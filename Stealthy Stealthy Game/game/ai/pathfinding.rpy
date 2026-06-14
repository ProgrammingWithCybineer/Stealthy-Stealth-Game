
init python:

    def move_towards(entity, target_x, target_y, speed=2):

        if entity.x < target_x:
            entity.x += speed

        if entity.x > target_x:
            entity.x -= speed

        if entity.y < target_y:
            entity.y += speed

        if entity.y > target_y:
            entity.y -= speed

            