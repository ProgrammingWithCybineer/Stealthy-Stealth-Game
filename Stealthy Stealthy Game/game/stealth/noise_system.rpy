

init python:

    def create_footstep_noise():

        volume = 50

        if not player.crouched:
            volume = 150

        generate_noise(
            player.x,
            player.y,
            volume
        )

        