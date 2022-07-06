import pygame
 
pygame.init()

# Config Game Variable
Run_Game = True # False if you dont wan it to run 
pygame.display.set_caption('C2C Project')

#Global Game Variables 
player_list = pygame.sprite.Group()

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

# OOP CLasses Creation
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 48
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Color_White)
        self.rect = self.image.get_rect()


# PLayerHAndler 
Main_Player = Player()
Main_Player.rect.x = 0
Main_Player.rect.y = 0 
player_list.add(Main_Player)

while Run_Game:
    The_World.fill(Color_Green)
    player_list.draw(The_World)
    pygame.display.flip()
    Clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run_Game = False

        if event.type == pygame.KEYDOWN:
            # Handle Quiting
            if event.key == ord('q'):
                pygame.quit()
                Run_Game = False

            # Handle Movement
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("Left")
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("Right")
            elif event.key == pygame.K_UP or event.key == ord('w'):
                print("Up")
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                print("Down")

        if event.type == pygame.KEYUP:
            # Handle Movement 
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("Left Stop")
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("Right Stop")
            elif event.key == pygame.K_UP or event.key == ord('w'):
                print("Up Stop")
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                print("Down Stop")


        
