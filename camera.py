

class Camera:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.viewport_width = width
        self.viewport_height = height

    def follow(self,player):
        self.x = player.center_x - self.viewport_width / 2
        self.y = player.center_y -  self.viewport_height / 2