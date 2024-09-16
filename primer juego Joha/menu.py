import pygame
import constantes
#personaje
from personaje import Personaje
#arma
from weapon import Weapon
pygame.init()

#ventana del juego
ventana = pygame.display.set_mode((constantes.ANCHO_VEN, constantes.ALTO_VEN))
#nombre del juego
pygame.display.set_caption("Mi juego Joha")
#personaje con imagenes
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return  nueva_imagen

#Importar imagenes:
    #Personaje
animaciones = []
for i in range (7):
    img = pygame.image.load(f"assets//images//characters//player//walk_{i}.png").convert_alpha()
    img = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)

    #Arma convert alpha, para que se vean bien los png
imagen_pistola = pygame.image.load(f"assets//images//weapons//arma.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)
#crear un jugador de la clase personaje
jugador = Personaje(50, 50, animaciones)

#crear un arma del jugador de la clase weapon
pistola = Weapon(imagen_pistola)

#Definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False
#frames por segundo
reloj = pygame.time.Clock()

#conservar venta abierta
run = True
while run == True:
#Tiempo de moviemiento en frames
    reloj.tick(constantes.FPS)
# Fondo
    ventana.fill(constantes.COLOR_BG)
#Calcular movimiento del jugador
    delta_x = 0
    delta_y = 0
    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
#ejecutando movimiento
    jugador.movimiento(delta_x, delta_y)
#Actualiza estado del jugador
    jugador.update()
#Actualiza el estado del arma
    pistola.update(jugador)

#mostrar al personaje en la ventana
    jugador.dibujar(ventana)
#mostar el arma
    pistola.dibujar(ventana)


#Cerrar ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Reconocieminto de movimiento por teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
#Para cuando se deja de pulsar la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False


#actualizar ventana
    pygame.display.update()

pygame.quit()