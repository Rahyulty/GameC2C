import pygame
 
pygame.init()

# COnfig Game Variable
Run_Game = True # False if you dont wan it to run 


# Setting up our screen
World_X = 800
World_Y = 600
FPS = 40
Clock = pygame.time.Clock()

# Setting Up Colors
Color_Blue = (25, 25, 200)
Color_Black = (23, 23, 23)
Color_White = (254, 254, 254)
Color_Green = (86, 125, 70)

The_World = pygame.display.set_mode([World_X, World_Y])


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 48
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Color_White)
        self.rect = self.image.get_rect()

while Run_Game:
    The_World.fill(Color_Green)
    pygame.display.flip()
    Clock.tick(FPS)
