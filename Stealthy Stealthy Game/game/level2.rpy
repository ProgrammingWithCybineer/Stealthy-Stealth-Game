

label level2:

    scene black

    "Mission 2"

    "Infiltrate the Treasury."

    $ guards.append(Guard(900,200,250))

    show screen stealth_game

    while True:

        if alarm_active:

            "Mission Failed"

            return

        pause 0.1