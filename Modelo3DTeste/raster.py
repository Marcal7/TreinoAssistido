import cv2
import mediapipe as mp
import numpy as np
import pandas as pd

# Inicializando o BlazePose e o desenhador
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Inicializar captura de vídeo
cap = cv2.VideoCapture('../dunk.mp4')

# Lista para armazenar os dados dos landmarks
landmarks_data = []
frame_index = 0

# Nomes dos pontos de interesse do corpo humano (33 landmarks no BlazePose)
landmark_names = [
    "left_eye", "right_eye", "left_shoulder", "right_shoulder", "left_elbow",
    "right_elbow", "left_arm", "right_arm", "left_wrist", "right_wrist", "left_pinky", "right_pinky", "left_index", "right_index",
    "left_thumb", "right_thumb", "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle",
    "left_heel", "right_heel", "left_foot_index", "right_foot_index"
]

# Abrir Pose Estimator
with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Converter imagem para RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        # Verificar se landmarks foram detectadas
        if results.pose_landmarks:
            # Extrair as coordenadas dos landmarks
            landmarks = results.pose_landmarks.landmark
            frame_data = {'frame': frame_index}  # Adicionar o índice do frame

            for i in range(len(landmarks)):  # Use o tamanho real da lista landmarks
                if i < len(landmark_names):  # Verifique se o índice está dentro dos limites
                    landmark = landmarks[i]
                    frame_data[f"{landmark_names[i]}_x"] = landmark.x
                    frame_data[f"{landmark_names[i]}_y"] = landmark.y
                    frame_data[f"{landmark_names[i]}_z"] = landmark.z

            landmarks_data.append(frame_data)  # Adicionar os dados do frame à lista
            frame_index += 1

            # Desenhar os pontos da pose
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Exibir frame processado
        cv2.imshow('BlazePose', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()

# Converter dados para um DataFrame e salvar em CSV
landmarks_df = pd.DataFrame(landmarks_data)
landmarks_df.to_csv('landmarks.csv', index=False)

print("Dados dos landmarks extraídos e salvos com sucesso!")

exit()