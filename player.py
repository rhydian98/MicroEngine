import pygame
from entity import Entity
class Player(Entity):
    def __init__(self, width, height, x, y, color, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed


        self.get_sides()

    def contain_within_bounds(self, width, height):
        if self.x < 0:
            self.x = 0
        if self.x + self.width > width:
            self.x = width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > height:
            self.y = height - self.height

    def move_x(self,keys, adjusted_speed, solids):
        old_x = self.x
        
        if keys[pygame.K_d]:
            self.x += adjusted_speed
        if keys[pygame.K_a]:
            self.x -= adjusted_speed

        for solid in solids:
            if self.collides_with(solid):
                self.handle_x_collision(old_x)
                break
    def move_y(self, keys, adjusted_speed, solids):
        old_y = self.y
        
        if keys[pygame.K_s]:
            self.y += adjusted_speed
        if keys[pygame.K_w]:
            self.y -= adjusted_speed
        for solid in solids:
            if self.collides_with(solid):
                self.handle_y_collision(old_y)
                break
        

    def update(self, keys,dt, solids):
        speed = self.speed*dt
        
        self.move_x(keys, speed, solids)
        self.move_y(keys, speed, solids)
        


        self.get_sides()
    
    def handle_x_collision(self, old_x):
        self.x = old_x

    def handle_y_collision(self, old_y):
        self.y = old_y

    def handle_collision(self, entity):

        if self.collides_with(entity):
            self.x = self.previous_x
            self.y = self.previous_y
        
        
    
    