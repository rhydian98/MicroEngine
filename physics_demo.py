from engine.camera import Camera
from engine.world import World
import engine.constants
from engine.dynamic_entity import DynamicEntity
from engine.game import Game
import pygame

class PhysicsBody(DynamicEntity):

    def __init__(self, tile_width, tile_height, x, y, color, mass=1.0, bounciness = 0.8):
        super().__init__(tile_width, tile_height, x, y, color)
        
        self.velocity_x = 0.0
        self.velocity_y = 0.0

        self.acceleration_x = 0.0
        self.acceleration_y = 0.0

        self.mass = mass
        self.bounciness = bounciness


    def update(self,dt, solids ):
        super().update_motion(dt, solids)

        self.resolve_bounce(self.mass, self.velocity_x, self.velocity.y)


    def resolve_bounce(self, mass, velocity_x, velocity_y):
        


def game_loop(game, world):
    camera = Camera(0, 0, 800,600)
    running = True
    screen = game.screen
    clock = pygame.Clock()
    

    body = PhysicsBody(1, 1, 1, 1, (255, 0, 0))
    
    body.velocity_x = 200
    body.velocity_y = 100

    body.acceleration_y = 900


    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        body.update(dt)
        #camera.follow(body)
        screen.fill((30,30,30))
        
        
        body.draw(screen, camera)
        
        pygame.display.flip()



def main():
    game = Game(800, 600)
    world = World(2400,1800)
    
    game_loop(game, world)
        



if __name__ == "__main__":
    main()
        
