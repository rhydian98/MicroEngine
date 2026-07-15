import pygame
import os
from engine.dynamic_entity import DynamicEntity
from engine.constants import TILE_HEIGHT, TILE_WIDTH
class Player(DynamicEntity):

    def __init__(self, width, height, x, y, color, move_acceleration):
    
        super().__init__(width, height, x, y, color)

        
        self.load_sprite()
        self.move_acceleration = move_acceleration

    @property
    def column(self):
        return self.x // TILE_WIDTH
    
    @property
    def row(self):
        return self.y // TILE_HEIGHT

        
    

    def get_input(self, keys):

        self.acceleration_x = 0.0
        self.acceleration_y = 0.0

        if keys [pygame.K_a]:
            self.acceleration_x = -self.move_acceleration
        elif keys [pygame.K_d]:
            self.acceleration_x = self.move_acceleration

        if keys [pygame.K_s]:
            self.acceleration_y = self.move_acceleration
        elif keys [pygame.K_w]:
            self.acceleration_y = -self.move_acceleration
        
        
        

    def load_sprite(self):
        print(os.getcwd())
        self.sprite_sheet = pygame.image.load("assets/NPC Merchant-idle.png").convert_alpha()

        frame = pygame.Rect(0, 0, 110, 110)
        self.image = self.sprite_sheet.subsurface(frame)

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    