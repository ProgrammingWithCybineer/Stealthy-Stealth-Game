

init python:

    def visibility_score(light_level):

        shadow_bonus = 50

        if player.hidden:
            shadow_bonus += 40

        return max(0, light_level - shadow_bonus)

    