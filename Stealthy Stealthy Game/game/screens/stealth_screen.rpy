
screen stealth_game():

    add "maps/castle_hall.png"

    add "player.png" xpos player.x ypos player.y

    for guard in guards:

        add "guard.png" xpos guard.x ypos guard.y

    text "Hidden: [player.hidden]" xpos 10 ypos 10

    text "Inventory: [len(player.inventory)]" xpos 10 ypos 40

    key "K_UP" action Function(player.move,0,-10)
    key "K_DOWN" action Function(player.move,0,10)
    key "K_LEFT" action Function(player.move,-10,0)
    key "K_RIGHT" action Function(player.move,10,0)

    timer 0.25 repeat True action Function(check_hiding)

    timer 0.25 repeat True action If(
        check_detection(),
        Function(trigger_alarm)
    )