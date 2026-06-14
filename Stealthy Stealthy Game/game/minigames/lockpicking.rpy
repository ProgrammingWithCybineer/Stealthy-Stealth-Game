

init python:

    class Lock:

        def __init__(self):

            self.pins = [False] * 5

        def complete(self):

            return all(self.pins)

        