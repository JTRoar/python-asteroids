import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import *


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
    asteroids = pygame.sprite.Group()
    #Player is name of class, not an instance of it
    #this must be done before any player objects are created
    Player.containers = (
        updatable, #all the objects that can be updated
        drawable   #all the objects that can be drawn
        )
    
    Asteroid.containers = (
        asteroids,
        updatable,
        drawable,
    )
    #create asteroid field container, only add to updatable
    AsteroidField.containers = updatable 

    #create new asteroidfield object
    asteroid_field = AsteroidField()



    #use the player class created in player.py
    player_object = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)) 
    
    while True:
        log_state()
        log_event("player_hit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##allow you to exit out by clicking X
                return
        
        #Game logic and drawing goes here 
        screen.fill("black") #set background screen to black
        
        updatable.update(dt) ## same as the for loop i was doing, but how it was meant to be written?
        
        for asteroid in asteroids:
            if asteroid.collides_with(player_object):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for object in drawable:  #draw all the drawables
            object.draw(screen)
        
        #Call .tick(60) at the end of the loop and divide return value by 1000 to get ms, and save to dt "Delta time"
        dt = clock.tick(60) / 1000 #set the FPS to 60
        
        pygame.display.flip() #refreshes the screen, always call last
        


if __name__ == "__main__":
    main()
