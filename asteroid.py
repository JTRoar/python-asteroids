import pygame
import random 
from logger import log_event
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt): 
        self.position += self.velocity * dt 

    def split(self):
        self.kill() #kill the current asteroid that was just shot
        if self.radius <= ASTEROID_MIN_RADIUS:
            return #end method and return, because it was a small asteroid that no longer splits
        else:
            log_event("asteroid_split") #register new log event
            #calculate new angle for the splitting asteroids
            #a new angle, thus the variables below, will be called / changed
            #everytime split() is run
            random_angle = random.uniform(20, 50) #get a random number between 20 and 50 for the new degree of flight
            #create new vectors. Use pygame's .rotate and the random angle
            #one negative, one positive
            first_new_vector = self.velocity.rotate(random_angle)
            second_new_vector = self.velocity.rotate(-random_angle)
            #check for a new radius. We only have Large, Medium, and Small radius'
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #Create two new Asteroid Instances / objects of this class
            #notice we use the new_radius variable above to determine the size
            first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            #Speed them up. Large will be normal velocity, Medium will be * 1.2, and small 
            # will be the medium value further timesed by 1.2
            first_new_asteroid.velocity = first_new_vector * 1.2
            second_new_asteroid.velocity = second_new_vector * 1.2

           


