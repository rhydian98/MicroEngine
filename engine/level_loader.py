import json
from engine.player import Player
from engine.world import World
from engine.entity import Entity
def load_level(filename):
    with open(filename, "r") as file:
        data = json.load(file)

        world_data = data["world"]
        world = World(world_data["width"], world_data["height"])


        player_data = data["player_start"]
        player = Player(
            player_data["width"],
            player_data["height"],
            player_data["x"],
            player_data["y"],
            tuple(player_data["color"]),
            player_data["speed"]
        )

        walls = []
        for wall_data in data["walls"]:
            wall = Entity(
                wall_data["width"],
                wall_data["height"],
                wall_data["x"],
                wall_data["y"],
                tuple(wall_data["color"])

            )
            walls.append(wall)
        return world, player, walls