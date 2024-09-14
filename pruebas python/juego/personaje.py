#Personaje
import pygame
import constantes
#forma del personaje
class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, constantes.ALTO_PERSONAJE, constantes.ANCHO_PERSONAJE)
        self.forma.center = (x, y)
#movimiento del personaje
    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

#Dibujar personaje
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma)


