import cv2
import dlib
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

# Load the pre-trained face detector
detector = dlib.get_frontal_face_detector()

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        return img
    return None

def rescale_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

def update_image():
    img = load_image()
    if img is not None:
        scale_percent = scale_var.get()
        img = rescale_image(img, scale_percent)
        img = detect_faces(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img

# GUI setup
root = tk.Tk()
root.title("Image Converter and Face Tracker")

scale_var = tk.IntVar(value=100)
scale_label = tk.Label(root, text="Scale Percentage:")
scale_label.pack()
scale_entry = tk.Entry(root, textvariable=scale_var)
scale_entry.pack()

load_button = tk.Button(root, text="Load Image", command=update_image)
load_button.pack()

panel = tk.Label(root)
panel.pack()

root.mainloop()