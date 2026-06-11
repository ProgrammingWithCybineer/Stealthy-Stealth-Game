

screen inventory_screen():

    frame:

        xpos 400
        ypos 100

        vbox:

            text "Inventory"

            for item in player.inventory:

                text "[item.name]"