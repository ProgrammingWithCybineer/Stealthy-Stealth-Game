init python:

    hiding_spots = [
        (250, 200),
        (600, 350)
    ]

    def check_hiding():

        for spot in hiding_spots:

            if abs(player.x - spot[0]) < 40 and \
                abs(player.y - spot[1]) < 40:

                player.hide()
                return True

        player.unhide()
        return False