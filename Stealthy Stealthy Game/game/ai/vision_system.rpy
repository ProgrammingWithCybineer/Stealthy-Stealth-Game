


init python:

    def can_see_player(guard):

        if player.hidden:
            return False

        dx = abs(player.x - guard.x)
        dy = abs(player.y - guard.y)

        return dx < guard.vision_range and dy < 80

    