#external library imports
import pygame

#imports from engine
from engine.game import Game

def main():
    # Initialize Pygame
    pygame.init()
    game = Game(800, 600)

    game.game_loop()
    

    

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()