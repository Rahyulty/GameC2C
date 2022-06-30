import pygame
 
pygame.init()

# Game Variable
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


The_World = pygame.display.set_mode([World_X, World_Y])

while Run_Game:
    The_World.fill(Color_Blue)
    pygame.display.flip()
    Clock.tick(FPS)
