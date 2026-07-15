import pygame
from engine.camera import Camera
from engine.world import World
from pathlib import Path
import json
from engine.constants import TILE_HEIGHT, TILE_WIDTH

#walls variable global for now
walls = set()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Micro Engine Editor")
    camera = Camera(100,100, 800, 600)
    world = World(2400, 1800)
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                world_x = mouse_x + camera.x
                world_y = mouse_y + camera.y

                column  = int(world_x // TILE_WIDTH)
                row = int(world_y // TILE_HEIGHT)

                if event.button == 1:
                    walls.add((row, column))

                if event.button == 3:
                    walls.discard((row, column))

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        save_level(world, walls)

        update(camera)
        screen.fill((30, 30, 30))
        draw_grid(screen, camera, world)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()





def update(camera):
    keys = pygame.key.get_pressed()
    camera_speed = 250
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    movement = camera_speed * dt

    if keys[pygame.K_a]:
        camera.x -= movement
    if keys[pygame.K_d]:
        camera.x += movement
    if keys[pygame.K_w]:
        camera.y -= movement
    if keys[pygame.K_s]:
        camera.y += movement



def save_level(world, walls):
    level_name = input("Level Name: ").strip()

    if not level_name:
        print("Save Cancelled: no level name entered.")
        return
    
    if not level_name.endswith(".json"):
        level_name += ".json"


    filepath = Path("levels")/level_name

    wall_data = []

    for row, column in walls:
        wall_data.append({
            "column" : column,
            "row" : row,
            "tile_width" : 1,
            "tile_height" : 1,
            "color" : [0, 255, 0]
        })

    level_data = {
        "world": {
            "width": world.width,
            "height" : world.height

            },
        "player_start" : {
            "column" : 1,
            "row" : 1,
            "width" : 1,
            "height" : 1,
            "speed" : 300,
            "color" : [255, 0, 0]
            },
            
        "walls" : wall_data



        }

    filepath.parent.mkdir(parents = True, exist_ok = True)

    with filepath.open("w",  encoding="utf-8") as file:
        json.dump(level_data, file, indent=4)

    print(f"Saved file to {filepath}")
    
    

def draw_grid(screen, camera, world):
    grid_color = (80, 80, 80)

    columns = world.width // TILE_WIDTH
    rows = world.height // TILE_HEIGHT

    for column in range(columns + 1):
        world_x = column * TILE_WIDTH
        screen_x = world_x - camera.x

        pygame.draw.line(
            screen,
            grid_color,
            (screen_x, -camera.y),
            (screen_x, world.height - camera.y)
            )
    
    for row in range(rows+1):
        world_y = row * TILE_HEIGHT
        screen_y = world_y - camera.y


        pygame.draw.line(
            screen,
            grid_color,
            (-camera.x, screen_y),
            (world.width - camera.x, screen_y)

        )


    for row, column in walls:
        world_x = column * TILE_WIDTH
        world_y = row * TILE_HEIGHT

        screen_x = world_x - camera.x
        screen_y = world_y - camera.y

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (screen_x, screen_y, TILE_WIDTH, TILE_HEIGHT)
    )






if __name__ == "__main__":
    main()