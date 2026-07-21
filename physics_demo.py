from engine.camera import Camera
from engine.world import World
import engine.constants
from engine.components.motion import Motion
from engine.components.collider import Collider
from engine.components.physics import Physics
from engine.entity import Entity
from engine.level_loader import load_level
from engine.game import Game
import pygame
from pygame import Clock

class PhysicsBody(Entity):

    def __init__(self, tile_width, tile_height, x, y, color, mass=1.0, bounciness = 0.8, has_gravity=False):
        
        super().__init__(tile_width, tile_height, x, y, color)
        
        self.velocity_x = 200.0
        self.velocity_y = -100

        self.acceleration_x = 200.0
        self.acceleration_y = 0.0

        self.mass = mass
        self.bounciness = bounciness

        self.motion = Motion(max_velocity=1000, braking_force=2000)
        self.collider = Collider()
        self.physics = Physics(self.bounciness, has_gravity)


    def update(self,dt,solids):
        self.motion.reset_acceleration()
        self.physics.apply_gravity(self.motion)
        self.motion.accelerate(dt)
        
        self.motion.update(dt)

        dx, dy = self.motion.get_displacement(dt)

        hit_x = self.collider.move_x(self, self.motion, dx, solids)
        if hit_x:
            self.physics.handle_x_collision(self.motion)

        hit_y = self.collider.move_y(self, self.motion, dy, solids)
        if hit_y:
            self.physics.handle_y_collision(self.motion)

        



def physics_demo(game, world):
    screen = game.screen
    clock = pygame.time.Clock()

    # Fixed camera: do not call camera.follow().
    camera = Camera(0, 0, screen.get_width(), screen.get_height())

    # One test body. Adjust arguments to match your constructor.
    body = PhysicsBody(
        1,              # tile width
        1,              # tile height
        4,              # starting column/x
        2,              # starting row/y
        (255, 80, 80),  # colour
        bounciness=0.8,
        has_gravity=True,
    )

    # Initial sideways velocity so both axes can be tested.
    body.motion.velocity_x = 250.0
    body.motion.velocity_y = 0.0

    # Temporary manually-created walls.
    # Adjust Entity arguments if yours differ.
    floor = Entity(16, 1, 0, 10, (80, 200, 80))
    left_wall = Entity(1, 10, 0, 0, (80, 200, 80))
    right_wall = Entity(1, 10, 15, 0, (80, 200, 80))

    solids = [floor, left_wall, right_wall]

    running = True

    while running:
        dt = clock.tick(60) / 1000.0

        # Prevent a large physics jump if the window stalls.
        dt = min(dt, 0.05)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        body.update(dt, solids)

        # Draw
        screen.fill((30, 30, 30))

        for solid in solids:
            solid.draw(screen, camera)

        body.draw(screen, camera)

        pygame.display.flip()

    pygame.quit()
        



def main():
    game = Game(800, 600, "levels/physics.json")
    world= World(800,600)
    
    physics_demo(game,world)
        



if __name__ == "__main__":
    main()
        
