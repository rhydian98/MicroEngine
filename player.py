import pygame

class Player():
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def contain_within_bounds(self, width, height):
        if self.x < 0:
            self.x = 0
        if self.x + self.width > width:
            self.x = width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > height:
            self.y = height - self.height

    def update(self, keys):

        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_a]:
            self.x -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_d]:
            self.x += 1
        
        
    
    def draw(self,screen):
        pygame.draw.rect(screen,  self.color, (self.x, self.y, self.width, self.height) )