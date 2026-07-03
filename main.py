import pygame
from player import Player
def draw_rectangle(screen,height, width, position, color):
    pygame.draw.rect(screen, color, (position[0], position[1], width, height))



def create_window(width, height):
    # Set up the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Pygame Window")

    return screen


def game_loop(screen, width, height):
    # Main loop
    player = Player(100, 100, 100, 100, (255, 0, 0))
    running = True
    position = [100, 100]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        keys = pygame.key.get_pressed()
        player.update(keys)
        player.contain_within_bounds(width, height)
        


        # Fill the screen with a color (RGB)
        screen.fill((0, 128, 255))
        #draw rectangle on screen
        player.draw(screen)
        # Update the display
        pygame.display.flip()

def main():
    # Initialize Pygame
    pygame.init()

    screen = create_window(800, 600)

    game_loop(screen, 800, 600)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()