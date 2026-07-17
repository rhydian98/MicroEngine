import pygame
from engine.camera import Camera
from engine.constants import TILE_HEIGHT, TILE_WIDTH

class Entity:
    def __init__(self, tile_width, tile_height, x, y, color):
        self.x = x * TILE_WIDTH
        self.y = y * TILE_HEIGHT
        self.width = tile_width * TILE_WIDTH
        self.height = tile_height * TILE_HEIGHT
        self.color = color
        self.image = None

    

    @property
    def left(self):
        return self.x
    @property
    def right(self):
        return self.x + self.width
    @property
    def top(self):
        return self.y
    @property
    def bottom(self):
        return self.y + self.height
    @property
    def center_x(self):
        return self.x + (self.width/2)
    @property
    def center_y(self):
        return self.y + (self.height/2)



    def draw(self,screen,camera):
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y

        if self.image:
            screen.blit(self.image, (screen_x, screen_y))
        else:
            pygame.draw.rect(screen,  self.color, (screen_x, screen_y, self.width, self.height) )


    def collides_with(self, entity):
        #print("Checking collision")
        if self.bottom > entity.top and self.left < entity.right and self.top < entity.bottom and self.right > entity.left:
            print("Colliding")
            return True
        return False