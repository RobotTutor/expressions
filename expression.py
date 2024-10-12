# Example file showing a circle moving on screen
import pygame 
from pygame import Rect
import socket



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


    


# Define the host and port
HOST = '0.0.0.0'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print(f"Listening on {HOST}:{PORT}...")

    while True:
        # Accept a connection
        conn, addr = s.accept()
       
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Buffer size
                if not data:
                    break
                print(f"Received: {data.decode()}")
                # print(type(data.decode()))
                if data.decode() == '0':
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
                # Optionally, send a response
                conn.sendall(data)  # Echo back the received data
    






pygame.quit()


