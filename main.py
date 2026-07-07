import pygame
from player import Player
from pygame import Clock
from entity import Entity
from camera import Camera
from world import World

def create_window(width, height):
    # Set up the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Pygame Window")

    return screen


def game_loop(screen, width, height):
    # Main loop
    camera = Camera(0, 0, 800, 600)
    world = World(2000, 2000, "Milk Land")
    wall = Entity(450, 50, 50, 0, (0, 255, 0))
    wall2 = Entity(50,220 ,450 , 50, (0, 255, 0))
    wall3 = Entity(450, 45,0 , 400, (0, 255, 0))
    wall4 = Entity(50, 400, 0,0, (0,255, 0))
    player = Player(100, 100, 50, 50, (255, 0, 0),250)

    entities = [player, wall, wall2, wall3, wall4]
    solids = [wall, wall2, wall3, wall4]
    running = True
    clock = Clock()
    dt = clock.tick(60)/1000
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # update player and collision detection
        player.update(keys,dt, solids)
        player.contain_within_bounds(world)
        camera.follow(player)
        camera.camera_bounds(world)
        # Fill the screen with a color (RGB)
        screen.fill((0, 128, 255))
        #draw entities
        for entity in entities:
            entity.draw(screen, camera)
        # Update the display
        pygame.display.flip()
        clock.tick(60)

def main():
    # Initialize Pygame
    pygame.init()

    screen = create_window(800, 600)

    game_loop(screen, 800, 600)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()