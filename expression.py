# Example file showing a circle moving on screen
import pygame 
from pygame import Rect

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()
running = True

left_eye_pos = pygame.Vector2((screen.get_width()/2)+100,130)
right_eye_pos = pygame.Vector2((screen.get_width()/2)-100,130)
rect = (380, 280, 120, 100)


def mouse_position():
    print(pygame.mouse.get_pos())

x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # pygame.draw.circle(screen,'blue', left_eye_pos, 50)
    # pygame.draw.circle(screen,'blue', right_eye_pos, 50)
    # pygame.draw.arc(screen,'blue',rect,100,100,1000)
    pygame.draw.arc(screen, 'blue', rect, 190, 350, 100)
    
    # pygame.draw.circle()
    pygame.display.update()
    pygame.display.flip()
    # pygame.draw.circle(screen, "red", player_pos, 40)
    
    # flip() the display to put your work on screen
    # limits FPS to 60``
    mouse_position()    

pygame.quit()

