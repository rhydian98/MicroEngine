import pygame

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.get_sides()


    def get_sides(self):
        self.left = self.x
        self.top = self.y
        self.right = self.x + self.width
        self.bottom = self.y + self.height



    def draw(self,screen):
        pygame.draw.rect(screen,  self.color, (self.x, self.y, self.width, self.height) )


    def collides_with(self, entity):
        print("Checking collision")
        if self.bottom > entity.top and self.left < entity.right and self.top < entity.bottom and self.right > entity.left:
            print("Colliding")
            return True