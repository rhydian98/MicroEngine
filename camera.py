

class Camera:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.viewport_width = width
        self.viewport_height = height

    def follow(self,player):
        self.x = player.center_x - self.viewport_width / 2
        self.y = player.center_y -  self.viewport_height / 2

    def camera_bounds(self, world):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.viewport_width > world.width:
            self.x = world.width - self.viewport_width 
        if self.y + self.viewport_height > world.height:
            self.y = world.height - self.viewport_height 

    