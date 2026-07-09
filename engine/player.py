import pygame
import os
from engine.entity import Entity
from engine.constants import TILE_HEIGHT, TILE_WIDTH
class Player(Entity):

    def __init__(self, width, height, x, y, color, speed):
        
        self.width = width * TILE_WIDTH
        self.height = height * TILE_HEIGHT
        self.x = x * TILE_WIDTH
        self.y = y * TILE_HEIGHT
        self.color = color
        self.speed = speed
        self.load_sprite()
    

    @property
    def column(self):
        return self.x // TILE_WIDTH
    
    @property
    def row(self):
        return self.y // TILE_HEIGHT

        
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
        
        

    def load_sprite(self):
        print(os.getcwd())
        self.sprite_sheet = pygame.image.load("assets/NPC Merchant-idle.png").convert_alpha()

        frame = pygame.Rect(0, 0, 110, 110)
        self.image = self.sprite_sheet.subsurface(frame)

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    