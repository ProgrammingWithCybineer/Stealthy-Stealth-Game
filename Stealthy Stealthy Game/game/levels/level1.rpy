

label level1:

    scene black

    "Mission 1"

    "Steal the King's Documents."

    show screen stealth_game
    show screen hud

    $ add_item(Item("Lockpick"))

    while True:

        if alarm_active:

            hide screen stealth_game

            "You were caught."

            return

        pause 0.1