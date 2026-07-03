import pygame

class Player():
    def __init__(self, width, height, x, y, color, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def contain_within_bounds(self, width, height):
        if self.x < 0:
            self.x = 0
        if self.x + self.width > width:
            self.x = width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > height:
            self.y = height - self.height

    def update(self, keys,dt):
        speed = self.speed*dt
        if keys[pygame.K_w]:
            self.y -= speed
        if keys[pygame.K_a]:
            self.x -= speed
        if keys[pygame.K_s]:
            self.y += speed
        if keys[pygame.K_d]:
            self.x += speed
        
        
    
    def draw(self,screen):
        pygame.draw.rect(screen,  self.color, (self.x, self.y, self.width, self.height) )