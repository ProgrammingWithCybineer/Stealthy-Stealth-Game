
screen pause_menu():

    frame:

        xalign 0.5
        yalign 0.5

        vbox:

            textbutton "Resume" action Hide("pause_menu")

            textbutton "Save" action ShowMenu("save")

            textbutton "Load" action ShowMenu("load")

            textbutton "Preferences" action ShowMenu("preferences")

            textbutton "Main Menu" action MainMenu()