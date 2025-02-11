import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace
from collections import deque

# ========================
# Configuración de MediaPipe para manos
# ========================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Diccionario para almacenar el historial de la posición x de la muñeca (landmark 0) de cada mano
wrist_histories = {}

# ========================
# Función para clasificar el gesto de la mano (abierta o cerrada)
# ========================
def clasificar_gesto(landmarks):
    # Se utiliza la distancia entre la muñeca (landmark 0) y la punta del dedo índice (landmark 8)
    wrist = np.array([landmarks[0].x, landmarks[0].y])
    index_tip = np.array([landmarks[8].x, landmarks[8].y])
    distancia = np.linalg.norm(index_tip - wrist)
    if distancia > 0.2:
        return "mano_abierta"
    else:
        return "mano_cerrada"

# ========================
# Función para analizar el rostro usando DeepFace (detectar emoción)
# ========================
def analizar_rostro(frame):
    try:
        # Se analiza el cuadro completo; en producción conviene extraer la región del rostro para mayor eficiencia.
        analisis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(analisis, list):
            emocion = analisis[0]['dominant_emotion']
        else:
            emocion = analisis['dominant_emotion']
        return emocion
    except Exception as e:
        return "Sin análisis"

# ========================
# Captura de video en tiempo real
# ========================
cap = cv2.VideoCapture(0)  # Usa la cámara por defecto

if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

print("Iniciando detección de gestos y análisis facial... (Presiona 'Esc' para salir)")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar el frame para facilitar el procesamiento
    frame = cv2.resize(frame, (640, 480))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ---- Análisis Facial ----
    emocion = analizar_rostro(frame)
    cv2.putText(frame, f"Emocion: {emocion}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # ---- Detección de Manos y Gestos ----
    results = hands_detector.process(frame_rgb)

    if results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Dibujar landmarks y conexiones de la mano en el frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Actualizar historial de posición horizontal (x) para la muñeca (landmark 0)
            if i not in wrist_histories:
                wrist_histories[i] = deque(maxlen=10)
            wrist_histories[i].append(hand_landmarks.landmark[0].x)

            # Si el historial está completo, se verifica si hay oscilación (gesto de saludar)
            if len(wrist_histories[i]) == wrist_histories[i].maxlen:
                if max(wrist_histories[i]) - min(wrist_histories[i]) > 0.1:  # Umbral ajustable
                    gesture = "saludar"
                else:
                    gesture = clasificar_gesto(hand_landmarks.landmark)
            else:
                gesture = clasificar_gesto(hand_landmarks.landmark)

            # Ubicar el texto cerca de la muñeca
            x = int(hand_landmarks.landmark[0].x * frame.shape[1])
            y = int(hand_landmarks.landmark[0].y * frame.shape[0])
            cv2.putText(frame, gesture, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    else:
        # Si no se detectan manos, se limpia el historial
        wrist_histories.clear()

    # Mostrar el resultado en una ventana
    cv2.imshow("IA - Reconocimiento Facial y Gestos", frame)

    # Salir con la tecla Esc
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()