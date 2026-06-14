

init python:

    def check_detection():

        if player.hidden:
            return False

        for guard in guards:

            dx = abs(player.x - guard.x)
            dy = abs(player.y - guard.y)

            if dx < guard.vision_range and dy < 80:

                guard.alerted = True
                return True

        return False

    