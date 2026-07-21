from .motion import Motion

class Physics:

    def __init__(self, bounciness, gravity=False):
        self.bounciness = bounciness
        self.gravity = gravity

    def handle_x_collision(self, motion):
        motion.velocity_x = -motion.velocity_x * self.bounciness

        if abs(motion.velocity_x) < 10:
            motion.velocity_x = 0

    def handle_y_collision(self, motion):
        motion.velocity_y = -motion.velocity_y * self.bounciness
        if abs(motion.velocity_y) < 10.0:
            motion.velocity_y = 0

    def apply_gravity(self, motion):
        if self.gravity:
            motion.acceleration_y += 1000