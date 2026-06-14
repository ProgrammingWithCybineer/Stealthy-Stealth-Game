
init python:

    class Drone:

        def __init__(self, x, y):

            self.x = x
            self.y = y

            self.active = True

        def patrol(self):

            self.x += 2

            