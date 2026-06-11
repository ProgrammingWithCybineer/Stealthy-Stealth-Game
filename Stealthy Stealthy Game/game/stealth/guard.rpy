
init python:

    class Guard:

        def __init__(self, x, y, vision_range):
            self.x = x
            self.y = y
            self.vision_range = vision_range
            self.alerted = False

        def patrol(self):
            self.x += 5

    guards = [
        Guard(400, 200, 150),
        Guard(700, 300, 200)
    ]