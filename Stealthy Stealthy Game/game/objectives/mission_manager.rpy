

init python:

    class Mission:

        def __init__(self, title):

            self.title = title
            self.completed = False

    active_mission = Mission(
        "Steal Documents"
    )

    def complete_mission():

        active_mission.completed = True

        