import pygame

from engine.entity import Entity

class Player(Entity):
    def __init__(self, width, height, x, y, color, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed


        
    def contain_within_bounds(self, world):
        if self.x < 0:
            self.x = 0
        if self.x + self.width > world.width:
            self.x = world.width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > world.height:
            self.y = world.height - self.height

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
        


        
    
    def handle_x_collision(self, old_x):
        self.x = old_x

    def handle_y_collision(self, old_y):
        self.y = old_y

    def handle_collision(self, entity):

        if self.collides_with(entity):
            self.x = self.previous_x
            self.y = self.previous_y
        
        
    
    