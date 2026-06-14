

init python:

    class Camera:

        def __init__(self, x, y):

            self.x = x
            self.y = y

            self.angle = 0
            self.active = True

        def update(self):

            self.angle += 2

    cameras = [
        Camera(500,100)
    ]

    