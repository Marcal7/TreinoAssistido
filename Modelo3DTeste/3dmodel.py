from vpython import sphere, cylinder, vector, rate, canvas
import numpy as np
import pandas as pd

# Carregar os dados do arquivo CSV
csv_file_path = '../landmarks.csv'
landmarks = pd.read_csv(csv_file_path)

scene = canvas(background=vector(0, 1, 0))  # Cor verde

'''left_eye", "right_eye", "left_shoulder", "right_shoulder", "left_elbow",
"right_elbow", "left_wrist", "right_wrist", "left_pinky", "right_pinky", "left_index", "right_index",
"left_thumb", "right_thumb", "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle",
"left_heel", "right_heel", "left_foot_index", "right_foot_index'''

# Criar um "homem de palito"
head = sphere(pos=vector(0, 0, 0), radius=0.1, color=vector(1, 0.8, 0.6))  # Cabeça
#neck = cylinder(pos=vector(0, -0.1, 0), axis=vector(0, -0.1, 0), radius=0.03, color=vector(0, 0, 0))  # Pescoço
left_shoulder = sphere(pos=vector(0, -0.2, 0.1), radius=0.02, color=vector(0, 0, 0))  # Ombro esquerdo
right_shoulder = sphere(pos=vector(0, -0.2, -0.1), radius=0.02, color=vector(0, 0, 0))  # Ombro direito
left_elbow = sphere(pos=vector(-0.2, -0.3, 0.1), radius=0.02, color=vector(0, 0, 0))  # Cotovelo esquerdo
right_elbow = sphere(pos=vector(0.2, -0.3, -0.1), radius=0.02, color=vector(0, 0, 0))  # Cotovelo direito
left_hand = sphere(pos=vector(-0.3, -0.4, 0.1), radius=0.02, color=vector(0, 0, 0))  # Mão esquerda
right_hand = sphere(pos=vector(0.3, -0.4, -0.1), radius=0.02, color=vector(0, 0, 0))  # Mão direita

# Criar os cilindros (ossos) para os braços
left_arm = cylinder(pos=left_shoulder.pos, axis=vector(-0.2, -0.1, 0), radius=0.025, color=vector(0, 0, 0))
right_arm = cylinder(pos=right_shoulder.pos, axis=vector(0.2, -0.1, 0), radius=0.025, color=vector(0, 0, 0))

# Criar a parte do corpo
body = cylinder(pos=vector(0, -0.3, 0), axis=vector(0, -0.4, 0), radius=0.04, color=vector(0, 0, 0))

# Criar as pernas
left_leg = cylinder(pos=body.pos, axis=vector(-0.1, -0.3, 0), radius=0.025, color=vector(0, 0, 0))
right_leg = cylinder(pos=body.pos, axis=vector(0.1, -0.3, 0), radius=0.025, color=vector(0, 0, 0))

# Animação
frames = len(landmarks)
while True:
    for frame in range(frames):
        rate(30)  # Limita a animação a 30 frames por segundo

        # Aplique os dados dos landmarks aos pontos do homem de palito
        head.pos = vector(landmarks['left_eye_x'][frame],
                          landmarks['left_eye_y'][frame] + 0.1,
                          landmarks['left_eye_z'][frame])

        left_shoulder.pos = vector(landmarks['left_shoulder_x'][frame],
                                   landmarks['left_shoulder_y'][frame],
                                   landmarks['left_shoulder_z'][frame])
        right_shoulder.pos = vector(landmarks['right_shoulder_x'][frame],
                                    landmarks['right_shoulder_y'][frame],
                                    landmarks['right_shoulder_z'][frame])

        left_elbow.pos = vector(landmarks['left_elbow_x'][frame],
                                landmarks['left_elbow_y'][frame],
                                landmarks['left_elbow_z'][frame])
        right_elbow.pos = vector(landmarks['right_elbow_x'][frame],
                                 landmarks['right_elbow_y'][frame],
                                 landmarks['right_elbow_z'][frame])

        left_hand.pos = vector(landmarks['left_wrist_x'][frame],
                               landmarks['left_wrist_y'][frame] - 0.1,
                               landmarks['left_wrist_z'][frame])
        right_hand.pos = vector(landmarks['right_wrist_x'][frame],
                                landmarks['right_wrist_y'][frame] - 0.1,
                                landmarks['right_wrist_z'][frame])

        left_arm.pos = vector(landmarks['left_arm_x'][frame],
                              landmarks['left_arm_y'][frame],
                              landmarks['left_arm_z'][frame])

        right_arm.pos = vector(landmarks['right_arm_x'][frame],
                               landmarks['right_arm_y'][frame],
                               landmarks['right_arm_z'][frame])

        body.pos = vector(landmarks['right_hip_x'][frame],
                          landmarks['right_hip_y'][frame] + 0.1,
                          landmarks['right_hip_z'][frame])

        left_leg.pos = vector(landmarks['left_knee_x'][frame],
                              landmarks['left_knee_y'][frame] - 0.1,
                              landmarks['left_knee_z'][frame])

        right_leg.pos = vector(landmarks['right_knee_x'][frame],
                               landmarks['right_knee_y'][frame] - 0.1,
                               landmarks['right_knee_z'][frame])
