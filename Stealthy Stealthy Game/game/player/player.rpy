
init python:

    class Player:

        def __init__(self):
            self.x = 100
            self.y = 100

            self.hidden = False
            self.crouched = False

            self.disguise = None
            self.nightvision = False

            self.inventory = []

        def move(self, dx, dy):

            self.x += dx
            self.y += dy

        def hide(self):
            self.hidden = True

        def unhide(self):
            self.hidden = False

    player = Player()

    