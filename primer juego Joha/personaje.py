#Personaje
import pygame
import constantes

#forma del personaje
class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
#imagen de la animacion que se muestra actualmente
        self.frame_index = 0
#hora actual milisegundos desde que se inicio pygame
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.forma = self.image.get_rect()
        self.forma.center = (x, y)
#movimiento del personaje
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
#guardar las animaciones
    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0


#Dibujar personaje
    def dibujar(self, interfaz):
        imagen_flit = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flit, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma,1)

