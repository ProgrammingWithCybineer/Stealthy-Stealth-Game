

screen stealth_game():

    add "images/maps/castle/map01.png"

    add "images/player/idle.png" xpos player.x ypos player.y

    for guard in guards:

        add "images/guards/guard.png" xpos guard.x ypos guard.y

    key "K_UP" action Function(player.move,0,-10)
    key "K_DOWN" action Function(player.move,0,10)
    key "K_LEFT" action Function(player.move,-10,0)
    key "K_RIGHT" action Function(player.move,10,0)

    timer 0.25 repeat True action Function(check_hiding)


    