import pygame
import os

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animaciones de Gestos")

# Cargar las animaciones
animations = {
    "saludar": "animaciones/saludo.mp4",
    "estrechar_mano": "animaciones/estrechar_mano.mp4",
    "pase_futbol": "animaciones/pase_futbol.mp4"
}

def play_animation(animation_path):
    # Aquí puedes usar un reproductor de video o simplemente reproducir un gif usando pygame
    # Para este ejemplo, usaremos solo una visualización simple, ya que pygame no maneja mp4 directamente
    # Asumamos que tienes un método para procesar y reproducir el video
    print(f"Reproduciendo: {animation_path}")
    # Aquí deberías integrar un reproductor de video o una biblioteca adecuada para reproducir el video

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                play_animation(animations["saludar"])
            elif event.key == pygame.K_2:
                play_animation(animations["estrechar_mano"])
            elif event.key == pygame.K_3:
                play_animation(animations["pase_futbol"])

    # Limpiar la pantalla
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()