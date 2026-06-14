

init python:

    class Item:

        def __init__(self, name):
            self.name = name

    def add_item(item):

        player.inventory.append(item)

    def remove_item(item):

        if item in player.inventory:
            player.inventory.remove(item)