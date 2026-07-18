import math
from engine.components.component import Component
class Motion(Component):

    def __init__(self, max_velocity = 300.0, braking_force = 0.0):
        self.velocity_x = 0.0
        self.velocity_y = 0.0

        self.acceleration_x = 0.0
        self.acceleration_y = 0.0

        self.max_velocity = max_velocity
        self.braking_force = braking_force

    def update(self, entity, dt):
        self.accelerate(dt)
        self.limit_velocity()
        self.move(entity, dt)

    def accelerate(self, dt):
        self.velocity_x += self.acceleration_x * dt
        self.velocity_y += self.acceleration_y * dt

    def move(self, entity, dt):
        entity.x += self.velocity_x * dt
        entity.y += self.velocity_y * dt

    def limit_velocity(self):
        speed = math.hypot(self.velocity_x, self.velocity_y)

        if speed > self.max_velocity:
            scale = self.max_velocity / speed
            self.velocity_x *= scale
            self.velocity_y *= scale

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

    def contain_within_bounds(self, entity, world):
        if entity.x < 0:
            entity.x = 0
        if entity.x + entity.width > world.width:
            entity.x = world.width - entity.width
        if entity.y < 0:
            entity.y = 0
        if entity.y + entity.height > world.height:
            entity.y = world.height - entity.height