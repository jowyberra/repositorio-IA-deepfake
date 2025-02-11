import cv2
import numpy as np
from deepfake_model import DeepFakeModel

# Initialize the deepfake model
model = DeepFakeModel()

# Load the animated format of the static image
animated_image = np.load('animated_image.npy')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the deepfake model to the webcam frame
    output_frame = model.apply(frame, animated_image)

    # Display the output frame
    cv2.imshow('DeepFake Animation', output_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()