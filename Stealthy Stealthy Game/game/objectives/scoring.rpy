

init python:

    class Score:

        def __init__(self):

            self.loot = 0
            self.detections = 0
            self.alarms = 0

        def total(self):

            return self.loot - \
                    (self.detections * 100) - \
                    (self.alarms * 250)

    score = Score()