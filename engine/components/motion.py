import math

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
            self.x += self.velocity_x * dt
            self.y += self.velocity_y * dt

        def limit_velocity():
            speed = math.hypot(self.velocity_x, self.velocity_y)

            if speed > self.max_velocity:
                scale = self.max_velocity / speed
                self.velocity_x *= scale
                self.velocity_y *= scale