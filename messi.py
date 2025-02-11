import cv2
import tkinter as tk
from PIL import Image, ImageTk
class MessiApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Messi Interactivo Automático")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        # Configurar cámara
        self.cap = cv2.VideoCapture(0)
        # Crear lienzo para mostrar cámara
        self.canvas = tk.Canvas(self.root, width=600, height=300, bg="lightblue")
        self.canvas.pack()
        # Cargar imágenes
        self.messi_img = ImageTk.PhotoImage(Image.open("messi.png").resize((100, 150)))
        self.ball_img = ImageTk.PhotoImage(Image.open("pelota.png").resize((50, 50)))
        # Colocar imagen inicial de Messi
        self.messi = self.canvas.create_image(50, 150, anchor=tk.CENTER, image=self.messi_img)
        # Iniciar detección
        self.detect_face_and_interact()
        self.root.mainloop()
    def detect_face_and_interact(self):
        # Cargar detector de rostros de OpenCV
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)  # Voltear para espejo
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detectar rostros
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            self.saludar()
        # Mostrar la cámara en el lienzo
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_tk = ImageTk.PhotoImage(Image.fromarray(frame))
        self.canvas.create_image(300, 150, anchor=tk.CENTER, image=img_tk)
        # Actualizar ventana
        self.root.after(50, self.detect_face_and_interact)
    def saludar(self):
        # Animación de saludo simple
        for _ in range(5):
            self.canvas.move(self.messi, 0, -5)
            self.root.update()
            self.root.after(50)
            self.canvas.move(self.messi, 0, 5)
            self.root.update()
            self.root.after(50)
# Ejecutar la aplicación
app = MessiApp()