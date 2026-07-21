from engine.camera import Camera
from pygame import Clock
import pygame
from engine.level_loader import load_level
class Game:

    def create_window(self ,width, height):
        # Set up the display
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("My Pygame Window")

        return screen
        
    def __init__(self, width, height, filename):
        self.screen = self.create_window(width, height)
        self.filename = filename
    
    def game_loop(self):
        # Main loop
        camera = Camera(0, 0, 800, 600)
        world, player, solids = load_level(self.filename)
        entities  = [player] + solids
        
        running = True
        clock = Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            dt = clock.tick(60)/1000

            keys = pygame.key.get_pressed()
            # update player and collision detection
            player.get_input(keys)
            player.update(keys, solids, dt, world)
            
            camera.follow(player)
            camera.camera_bounds(world)
            # Fill the screen with a color (RGB)
            self.screen.fill((0, 128, 255))
            #draw entities
            for entity in entities:
                entity.draw(self.screen, camera)
            # Update the display
            pygame.display.flip()
            clock.tick(60)