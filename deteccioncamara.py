import cv2
import mediapipe as mp
import numpy as np

# Inicializar Mediapipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configurar la captura de video
cap = cv2.VideoCapture(0)

# Inicializar el detector de caras y manos
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
hands = mp_hands.Hands(min_detection_confidence=0.5)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detección de caras
    results_faces = face_detection.process(frame_rgb)
    
    # Detección de manos
    results_hands = hands.process(frame_rgb)

    # Comprobar si hay caras detectadas
    if results_faces.detections:
        for detection in results_faces.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Usuario detectado', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Comprobar si hay manos detectadas
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Aquí se deben agregar condiciones para reconocer el gesto de saludo
            # Un ejemplo simple podría ser detectar si la mano está levantada
            # Nota: Implementar lógica para detectar si la mano está arriba de la cabeza

            # Si el gesto de saludo es detectado, se saluda al usuario
            cv2.putText(frame, '¡Hola!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el video
    cv2.imshow('Reconocimiento Facial y Gesto', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura
cap.release()
cv2.destroyAllWindows()