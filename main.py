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
    
    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #Player is name of class, not an instance of it
    #this must be done before any player objects are created
    Player.containers = (
        updatable, #all the objects that can be updated
        drawable   #all the objects that can be drawn
        )

    #use the player class created in player.py
    player_object = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)) 
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##allow you to exit out by clicking X
                return
        
        #Game logic and drawing goes here 
        screen.fill("black") #set background screen to black
        
        for object in drawable:  #draw all the drawables
            object.draw(screen)
        
        #Call .tick(60) at the end of the loop and divide return value by 1000 to get ms, and save to dt "Delta time"
        dt = clock.tick(60) / 1000 #set the FPS to 60
        
        #rotate the player object left and right
        for object in updatable:  #update all the updatables
            object.update(dt) 
        
        pygame.display.flip() #refreshes the screen, always call last
        


if __name__ == "__main__":
    main()
