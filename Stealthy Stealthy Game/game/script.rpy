##############################################################################
# Castle Shadows
# Main Entry Point
##############################################################################

define narrator = Character(None)

##############################################################################
# Defaults
##############################################################################

default game_started = False
default current_level = 1
default game_completed = False

##############################################################################
# Start
##############################################################################

label start:

    scene black

    with fade

    jump splash_screen

##############################################################################
# Splash Screen
##############################################################################

label splash_screen:

    scene black

    centered "Castle Shadows"

    pause 2.0

    jump main_menu

##############################################################################
# Main Menu
##############################################################################

label main_menu:

    scene black

    menu:

        "Castle Shadows"

        "New Game":

            jump new_game

        "Load Game":

            $ renpy.load()

        "Credits":

            jump credits

        "Quit":

            return

##############################################################################
# New Game
##############################################################################

label new_game:

    $ game_started = True

    $ current_level = 1

    jump intro

##############################################################################
# Intro Story
##############################################################################

label intro:

    scene black

    with fade

    narrator "The kingdom has fallen into corruption."

    narrator "Secrets are hidden behind castle walls."

    narrator "Tonight, you infiltrate the royal fortress."

    narrator "Your objective is simple."

    narrator "Do not get caught."

    jump mission_briefing

##############################################################################
# Mission Briefing
##############################################################################

label mission_briefing:

    scene black

    centered "MISSION 01"

    pause 1.0

    narrator "Objective: Steal the Royal Documents."

    narrator "Avoid guards and security systems."

    narrator "Reach extraction alive."

    jump level01

##############################################################################
# Level Router
##############################################################################

label next_level:

    if current_level == 1:

        jump level02

    elif current_level == 2:

        jump level03

    elif current_level == 3:

        jump boss_level

    else:

        jump ending

##############################################################################
# Game Over
##############################################################################

label game_over_screen:

    hide screen stealth_game

    hide screen hud

    hide screen objective_screen

    scene black

    centered "MISSION FAILED"

    pause 1.5

    menu:

        "Retry Mission":

            jump retry_level

        "Main Menu":

            jump main_menu

##############################################################################
# Retry Router
##############################################################################

label retry_level:

    if current_level == 1:

        jump level01

    elif current_level == 2:

        jump level02

    elif current_level == 3:

        jump level03

    elif current_level == 4:

        jump boss_level

##############################################################################
# Mission Complete
##############################################################################

label mission_complete:

    hide screen stealth_game

    hide screen hud

    hide screen objective_screen

    scene black

    centered "MISSION COMPLETE"

    pause 1.5

    show screen ranking_screen

    pause

    hide screen ranking_screen

    $ current_level += 1

    jump next_level

##############################################################################
# Ending
##############################################################################

label ending:

    scene black

    with fade

    narrator "The documents were recovered."

    narrator "The conspiracy was exposed."

    narrator "The kingdom has a chance to recover."

    narrator "You disappear into the shadows."

    $ game_completed = True

    centered "THE END"

    pause 2.0

    jump final_statistics

##############################################################################
# Statistics Screen
##############################################################################

label final_statistics:

    scene black

    centered "MISSION STATISTICS"

    pause 1.0

    "[score.total()] Total Score"

    "Detections: [score.detections]"

    "Alarms: [score.alarms]"

    "Loot: [score.loot]"

    jump credits

##############################################################################
# Credits
##############################################################################

label credits:

    scene black

    centered "Castle Shadows"

    pause 1.0

    centered "Programming"

    pause 1.0

    centered "You"

    pause 1.0

    centered "Built With Ren'Py"

    pause 2.0

    return

##############################################################################
# Global Gameplay Check
##############################################################################

label gameplay_loop:

    while True:

        if game_over:

            jump game_over_screen

        pause 0.1

##############################################################################
# Debug Menu (Optional)
##############################################################################

label debug_room:

    menu:

        "Debug"

        "Level 1":

            jump level01

        "Level 2":

            jump level02

        "Level 3":

            jump level03

        "Boss":

            jump boss_level

        "1000 Loot":

            $ score.loot += 1000

            jump debug_room

        "Back":

            jump main_menu