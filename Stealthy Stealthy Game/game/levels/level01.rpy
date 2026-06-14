

label level01:

    scene black

    "Mission 1"
    "Steal the royal documents."

    show screen stealth_game
    show screen hud

    while True:

        if check_detection():

            "You were detected."
            return

        pause 0.1

        