from .motion import Motion

class Collider:

    def move(self, entity, motion, dx, dy, solids, world):
        self.move_x(entity, motion, dx, solids)
        self.move_y(entity, motion, dy, solids)
        self.contain_within_bounds(entity, motion, world)


    def move_x(self, entity, motion, dx, solids):
        old_x  = entity.x
        entity.x += dx

        for solid in solids:
            if entity.collides_with(solid):
                entity.x = old_x
                motion.velocity_x = 0
                break

    def move_y(self, entity, motion, dy, solids):
        old_y = entity.y
        entity.y += dy

        for solid in solids:
            if entity.collides_with(solid):
                entity.y = old_y
                motion.velocity_y = 0
                break

    
    def contain_within_bounds(self, entity, motion, world):
        if entity.x < 0:
            entity.x = 0
        if entity.x + entity.width > world.width:
            entity.x = world.width - entity.width
        if entity.y < 0:
            entity.y = 0
        if entity.y + entity.height > world.height:
            entity.y = world.height - entity.height