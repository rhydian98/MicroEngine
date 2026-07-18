import pygame
import os
from engine.entity import Entity
from engine.constants import TILE_HEIGHT, TILE_WIDTH
from engine.components.motion import Motion
class Player(Entity):

    def __init__(self, width, height, x, y, color, move_acceleration):
        
        super().__init__(width, height, x, y, color)
        

        self.motion = Motion(
            max_velocity=300,
            braking_force=4000
        )
        
        self.load_sprite()
        self.move_acceleration = 2000
        

    @property
    def column(self):
        return self.x // TILE_WIDTH
    
    @property
    def row(self):
        return self.y // TILE_HEIGHT

    def update(self, keys, solids, dt, world):
        self.get_input(keys)
        self.motion.update(self, dt)
        
        
        if self.motion.acceleration_x == 0.0:
            self.motion.brake_x(dt)
        if self.motion.acceleration_y == 0.0:
            self.motion.brake_y(dt)


        
        self.motion.contain_within_bounds(self,world)

    

    def get_input(self, keys):

        self.motion.acceleration_x = 0.0
        self.motion.acceleration_y = 0.0

        if keys [pygame.K_a]:
            self.motion.acceleration_x = -self.move_acceleration
        elif keys [pygame.K_d]:
            self.motion.acceleration_x = self.move_acceleration

        if keys [pygame.K_s]:
            self.motion.acceleration_y = self.move_acceleration
        elif keys [pygame.K_w]:
            self.motion.acceleration_y = -self.move_acceleration
        


        
        
        

    def load_sprite(self):
        print(os.getcwd())
        self.sprite_sheet = pygame.image.load("assets/NPC Merchant-idle.png").convert_alpha()

        frame = pygame.Rect(0, 0, 110, 110)
        self.image = self.sprite_sheet.subsurface(frame)

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    