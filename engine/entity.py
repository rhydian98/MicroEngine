import pygame
from engine.camera import Camera

class Entity:
    def __init__(self, width, height, x, y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        

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
        pygame.draw.rect(screen,  self.color, (screen_x, screen_y, self.width, self.height) )


    def collides_with(self, entity):
        #print("Checking collision")
        if self.bottom > entity.top and self.left < entity.right and self.top < entity.bottom and self.right > entity.left:
            #print("Colliding")
            return True
        return False