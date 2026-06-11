
init python:

    alarm_active = False

    def trigger_alarm():

        global alarm_active

        alarm_active = True

        renpy.music.play(
            "audio/alert.ogg",
            channel="sound"
        )