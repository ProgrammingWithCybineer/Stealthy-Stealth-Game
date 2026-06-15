

label game_over_screen:

    hide screen stealth_game

    scene black

    centered "MISSION FAILED"

    pause 1.5

    menu:

        "Retry":
            jump level01

        "Main Menu":
            return