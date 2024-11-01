import mediapipe as mp
import cv2
import pandas as pd
import math
import numpy as np
import time
from datetime import datetime

# pip install openpyxl


def verificar_descanso(inicio_descanso, descanso):
    return time.time() - inicio_descanso >= descanso

count_rep = 0
count_se = 0
n_poli = 0
s_poli = 0
n_flex = 0
s_flex = 0
n_agacha = 0
s_agacha = 0

matricula = input("Insira a matrícula: ")

if matricula == "1":
    n_poli = 3
    s_poli = 1
    check_poli = True


    n_flex = 5
    s_flex = 1
    check_flex = True


    n_agacha = 5
    s_agacha = 1
    check_agacha = True

descanso = int(input("Insira o tempo de descanso (em segundos): "))
descanso_ativo = False
inicio_descanso = None

print("\n")

poli = input("Você irá fazer polichinelos? (sim/não): ")
check_poli = False
if poli.lower() == "sim":
    try:
        n_poli = int(input("Quantos polichinelos por série? "))
        s_poli = int(input("Quantas séries? "))
        check_poli = True

        print(f"Você realizará {s_poli} séries de {n_poli} polichinelos cada.")
    except ValueError:
        print("Por favor, digite um número válido.")
else:
    print("\n")

print("\n")

flex = input("Você irá fazer flexão? (sim/não): ")
check_flex = False
if flex.lower() == "sim":
    try:
        n_flex = int(input("Quantas flexões por série? "))
        s_flex = int(input("Quantas séries? "))
        check_flex = True

        print(f"Você realizará {s_flex} séries de {n_flex} polichinelos cada.")
    except ValueError:
        print("Por favor, digite um número válido.")
else:
    print("\n")

print("\n")

agacha = input("Você irá fazer agachamento? (sim/não): ")
check_agacha = False
if agacha.lower() == "sim":
    try:
        n_agacha = int(input("Quantos agachamentos por série? "))
        s_agacha = int(input("Quantas séries? "))
        check_agacha = True

        print(f"Você realizará {s_agacha} séries de {n_agacha} agachamentos cada.")
    except ValueError:
        print("Por favor, digite um número válido.")
else:
    print("\n")

novo_reg = []

# Inicializar o MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

iniciar = 'polichinelo'

inic = 1

webcan = True

# Criar um objeto para a detecção de poses
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened() and webcan is True:
        success, image = cap.read()
        if not success:
            print("Ignora efetuada pelo vídeo.")
            continue

        # Converter a imagem para RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False  # Desativar escrita na imagem

        # Processar a imagem e obter os landmarks
        results = pose.process(image)


        # Reativar a escrita na imagem
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Converter de volta para BGR

        # Desenhar os pontos de referência e as conexões entre eles
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            h, w, _ = image.shape
            points = results.pose_landmarks.landmark

            # Extração dos pontos
            peDY = int(points[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y * h)
            peDX = int(points[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x * w)
            peEY = int(points[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y * h)
            peEX = int(points[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x * w)
            moDY = int(points[mp_pose.PoseLandmark.RIGHT_INDEX].y * h)
            moDX = int(points[mp_pose.PoseLandmark.RIGHT_INDEX].x * w)
            moEY = int(points[mp_pose.PoseLandmark.LEFT_INDEX].y * h)
            moEX = int(points[mp_pose.PoseLandmark.LEFT_INDEX].x * w)
            nariz = int(points[mp_pose.PoseLandmark.NOSE].y * h)

            # Cálculo das distâncias
            distMO = math.hypot(moDX - moEX, moDY - moEY)
            distPE = math.hypot(peDX - peEX, peDY - peEY)
            distN_M = moEY - nariz
            distN_P = moDX - nariz

            #print(f'Mãos: {distMO}, Pés: {distPE}, C: {distN_M}, D: {distN_P}')

            if inic == 1:
                print("O programa irá iniciar em 5 segundos...")
                print("Se posicione a 1,5m da web cam")
                time.sleep(5)
                print("iniciando...")
                inic = 2

            if iniciar == 'polichinelo' and check_poli:

                if distMO <= 20 and distPE >= 100:

                    if not descanso_ativo:

                        count_rep += 1
                        print(count_rep)
                        time.sleep(0.3)

                        if count_rep >= n_poli:
                            count_rep = 0
                            count_se += 1

                            if count_se < s_poli:
                                print(f"Série {count_se} concluída. Descansando por {descanso} segundos.")
                                descanso_ativo = True
                                inicio_descanso = time.time()

                            else:
                                print("Concluido, polichinelo finalizado...\n")
                                check_poli = False
                                descanso_ativo = False
                                count_rep = 0
                                count_se = 0

                    else:
                        if descanso_ativo and verificar_descanso(inicio_descanso, descanso):
                            print(f"Descanso finalizado.\n")
                            descanso_ativo = False

            if check_poli is False:
                iniciar = 'flexao'

            if iniciar == 'flexao' and check_flex:

                if distN_M <= 50 and distMO > 100:

                    if not descanso_ativo:

                        count_rep += 1
                        print(count_rep)
                        time.sleep(1)

                        if count_rep >= n_flex:
                            count_rep = 0
                            count_se += 1

                            if count_se < s_flex:
                                print(f"Série {count_se} concluída. Descansando por {descanso} segundos.")
                                descanso_ativo = True
                                inicio_descanso = time.time()

                            else:
                                print("Concluido, flexão finalizada\n")
                                check_flex = False
                                descanso_ativo = False
                                count_rep = 0
                                count_se = 0

                else:
                    if descanso_ativo and verificar_descanso(inicio_descanso, descanso):
                        print(f"Descanso finalizado.\n")
                        descanso_ativo = False


            if iniciar == 'flexao' and check_flex is False:
                iniciar = 'agacha'

            if iniciar == 'agacha' and check_agacha:

                if distN_P <= 100 and distMO < 40:

                    if not descanso_ativo:

                        count_rep += 1
                        print(count_rep)
                        time.sleep(0.7)

                        if count_rep >= n_agacha:
                            count_rep = 0
                            count_se += 1

                            if count_se < s_agacha:
                                print(f"Série {count_se} concluída. Descansando por {descanso} segundos.")
                                descanso_ativo = True
                                inicio_descanso = time.time()

                            else:
                                print("Concluido, agachamento finalizado\n")
                                check_agacha = False
                                descanso_ativo = False
                                count_rep = 0
                                count_se = 0

                else:
                    if descanso_ativo and verificar_descanso(inicio_descanso, descanso):
                        print(f"Descanso finalizado.\n")
                        descanso_ativo = False

        # Mostrar a imagem
        cv2.imshow('MediaPipe Pose', image)

        if check_poli is False and check_poli is False and check_agacha is False:
            print("TREINO FINALIZADO")
            webcan = False

        # Parar o loop ao pressionar ESC
        if cv2.waitKey(5) & 0xFF == 27:
            break


# Liberar a captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()

novo_reg.append({
    "Matricula": matricula,
    "Data": datetime.now().strftime("%Y-%m-%d"),
    "Hora": datetime.now().strftime("%H:%M"),
    "N polichinelos": n_poli,
    "Série de polichinelos": s_poli,
    "N flexão": n_flex,
    "Série de flexão": s_flex,
    "N agacha": n_agacha,
    "Série de agachamento": s_agacha,
    "Descanso": descanso
})

df = pd.DataFrame(novo_reg)
df.to_excel(f"treino_{matricula}.xlsx", index=False)
print("Registro feito")

exit()