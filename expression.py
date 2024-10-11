# Example file showing a circle moving on screen
import pygame 
from pygame import Rect


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()
running = True

rect = (380, 280, 120, 100) 
timer = 1000

def update():
    pygame.display.update()
    pygame.display.flip()

def mouse_position():
    print(pygame.mouse.get_pos())

def clear_screen():
    screen.fill('black')
    pygame.display.flip()

def neutral_position():
    print('eye position neutral')

    #drawing left eye
    left_eye_pos = pygame.Rect((screen.get_width()/2)-175, (screen.get_width()/8), 100, 200)
    pygame.draw.rect(screen,'blue',left_eye_pos,border_radius=20)
    
    #drawing right eye
    right_eye_pos = pygame.Rect((screen.get_width()/2)+100, (screen.get_width()/8), 100, 200)
    pygame.draw.rect(screen,'blue',right_eye_pos,border_radius=20)
    
    #updating
    update()

def blinking_position():
    print('eye blinking')
    #drawing left eye
    left_eye_pos = pygame.Rect((screen.get_width()/2)-175, (screen.get_width()/4), 100, 100)
    pygame.draw.rect(screen,'blue',left_eye_pos,border_radius=20)

    #drawing right eye
    right_eye_pos = pygame.Rect((screen.get_width()/2)+100, (screen.get_width()/4), 100, 100)
    pygame.draw.rect(screen,'blue',right_eye_pos,border_radius=20)
    
    #updating
    update()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    neutral_position()
    pygame.time.wait(timer)
    clear_screen()
    
    blinking_position()
    pygame.time.wait(timer)


    pygame.display.update()
    pygame.display.flip()




pygame.quit()


