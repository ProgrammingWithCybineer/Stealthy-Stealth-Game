

init python:

    WALK_SPEED = 5
    RUN_SPEED = 10

    def move_player(dx, dy):

        speed = RUN_SPEED

        if player.crouched:
            speed = WALK_SPEED

        player.move(
            dx * speed,
            dy * speed
        )

        