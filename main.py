import pygame
from player import Player
from pygame import Clock
from entity import Entity
def draw_rectangle(screen,height, width, position, color):
    pygame.draw.rect(screen, color, (position[0], position[1], width, height))



def create_window(width, height):
    # Set up the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Pygame Window")

    return screen


def game_loop(screen, width, height):
    # Main loop
    wall = Entity(550, 300, 100, 250, (0, 255, 0))
    wall2 = Entity(300, 100, 200, 400, (0, 255, 0))
    wall3 = Entity(60, 200, 200, 60, (0, 255, 0))
    player = Player(100, 100, 100, 100, (255, 0, 0),250)

    entities = [player, wall, wall2, wall3]

    running = True
    clock = Clock()
    dt = clock.tick(60)/1000
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # update player and collision detection
        player.update(keys,dt, [wall, wall2, wall3])
        player.contain_within_bounds(width, height)
        
        # Fill the screen with a color (RGB)
        screen.fill((0, 128, 255))
        #draw entities
        for entity in entities:
            entity.draw(screen)
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