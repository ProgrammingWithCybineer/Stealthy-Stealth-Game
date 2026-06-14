

init python:

    checkpoint_data = {}

    def save_checkpoint():

        global checkpoint_data

        checkpoint_data = {
            "x": player.x,
            "y": player.y,
            "inventory": list(player.inventory)
        }

        