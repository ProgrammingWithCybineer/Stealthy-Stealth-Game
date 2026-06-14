

init python:

    class LockpickSet:

        def __init__(self):

            self.durability = 10

        def use(self):

            self.durability -= 1

            