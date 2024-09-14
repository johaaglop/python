import pygame
import constantes
#personaje
from personaje import Personaje
jugador = Personaje(50, 50)

pygame.init()
#ventana del juego
ventana = pygame.display.set_mode((constantes.ANCHO_VEN, constantes.ALTO_VEN))
#nombre del juego
pygame.display.set_caption("Mi juego Joha")

#Definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_Derecha = False

#conservar venta abierta
run = True
while run == True:
#Calcular movimiento del jugador
    delta_x = 0
    delta_y = 0
    if mover_arriba == True:
        delta_y = -5
    if mover_abajo == True:
        delta_y = 5
    if mover_izquierda == True:
        delta_x = -5
    if mover_Derecha == True:
        delta_x = 5
#ejecutando movimiento
    jugador.movimiento(delta_x, delta_y)


#mostrar al personaje en la ventana
    jugador.dibujar(ventana)
#Cerrar ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Reconocieminto de movimiento por teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda == True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mover_Derecha == True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mover_arriba == True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                mover_abajo == True

#actualizar ventana
    pygame.display.update()

pygame.quit()