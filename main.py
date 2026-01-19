import pygame
from constants import *
from logger import log_state
from player import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    
    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #clock object
    dt = 0
    #use the player class created in player.py
    player_object = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)) 
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##allow you to exit out by clicking X
                return
        
        #Game logic and drawing goes here
        screen.fill("black") #set background screen to black
        
        #draw player from parameters passed in player_object, which gets all the goods from Player class and inherited CircleShape parent
        player_object.draw(screen)
        #Call .tick(60) at the end of the loop and divide return value by 1000 to get ms, and save to dt "Delta time"
        dt = clock.tick(60) / 1000 #set the FPS to 60
        #print(dt) // may be useful to have in future
        #rotate the player object left and right
        player_object.update(dt) 
        pygame.display.flip() #refreshes the screen, always call last
        


if __name__ == "__main__":
    main()
