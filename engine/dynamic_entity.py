from engine.entity import Entity
import math
class DynamicEntity(Entity):

    def __init__(self, tile_width, tile_height, x, y, color, max_velocity=300.0):
        super().__init__(tile_width, tile_height, x, y, color)

        self.velocity_x = 0.0
        self.velocity_y = 0.0
        
        self.acceleration_x = 0.0
        self.acceleration_y = 0.0


        self.max_velocity = max_velocity

    def update_motion(self, dt, solids):

        


        self.accelerate_x(dt)
        self.accelerate_y(dt)

        self.limit_velocity()

        self.move_x(dt, solids)
        self.move_y(dt, solids)

    def move_x(self, dt,  solids):
        old_x = self.x
        self.x += self.velocity_x * dt

        for solid in solids:
            if self.collides_with(solid):
                self.handle_x_collision(old_x)
                break

    def move_y(self, dt, solids):
        old_y = self.y
        self.y += self.velocity_y * dt

        for solid in solids:
            if self.collides_with(solid):
                self.handle_y_collision(old_y)
                break
    
    def brake_x(self, dt):
        if self.velocity_x > 0:
            self.velocity_x = max(0, self.velocity_x - self.braking_force * dt)
        elif self.velocity_x < 0:
            self.velocity_x = min(0, self.velocity_x + self.braking_force * dt)

    def brake_y(self, dt):
        if self.velocity_y > 0:
            self.velocity_y= max(0, self.velocity_y - self.braking_force * dt)
        elif self.velocity_y < 0:
            self.velocity_y = min(0, self.velocity_y + self.braking_force * dt)


    
    def contain_within_bounds(self, world):
        if self.x < 0:
            self.x = 0
        if self.x + self.width > world.width:
            self.x = world.width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > world.height:
            self.y = world.height - self.height


    def accelerate_x(self, dt):
        self.velocity_x += self.acceleration_x * dt
        
    def accelerate_y(self, dt):
        self.velocity_y += self.acceleration_y * dt

    def limit_velocity(self):
        speed = math.hypot(self.velocity_x, self.velocity_y)

        if speed > self.max_velocity:
            scale = self.max_velocity / speed

            self.velocity_x *= scale
            self.velocity_y *= scale


    def handle_x_collision(self, old_x):
        self.velocity_x = 0
        self.x = old_x

    def handle_y_collision(self, old_y):
        self.velocity_y = 0
        self.y = old_y