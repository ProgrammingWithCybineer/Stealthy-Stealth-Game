
screen objective_screen():

    frame:

        xpos 20
        ypos 100

        vbox:

            text "Objective"

            text active_mission.title

            if active_mission.completed:
                text "Complete"

                