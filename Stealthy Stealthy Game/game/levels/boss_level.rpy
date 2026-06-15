

label boss_level:

    scene black

    "Final Mission"

    $ boss = BossGuard(
        800,
        300
    )

    show screen stealth_game

    while True:

        if boss.health <= 0:

            "Boss Defeated"

            return

        pause 0.1

        
