from .motion import Motion

class Physics:

    def __init__(self, bounciness):
        self.bounciness = bounciness

    def handle_x_collision(self, motion):
        motion.velocity_x = -motion.velocity_x * self.bounciness

    def handle_y_collision(self, motion):
        motion.velocity_y = -motion.velocity_y * self.bounciness

    def apply_gravity(self, motion):
        
            motion.acceleration_y += 1000