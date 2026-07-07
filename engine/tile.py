from constants import TILE_HEIGHT, TILE_WIDTH
class Tile():

    def __init__(self, row, column, color ):
        
        self.row = row
        self.column = column
        self.color = color


    @property
    def x(self):
        return self.row*TILE_WIDTH
    
    @property
    def y(self):
        return self.column * TILE_HEIGHT
    
    @property
    def width(self):
        return TILE_WIDTH
    
    @property
    def height(self):
        return TILE_HEIGHT