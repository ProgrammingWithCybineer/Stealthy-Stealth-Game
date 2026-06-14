

init python:

    import random

    def generate_castle():

        rooms = []

        for i in range(20):

            rooms.append(
                random.choice(room_templates)
            )

        return rooms

    