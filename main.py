import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            pass #//TODO update eventually
        screen.fill("black")
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
