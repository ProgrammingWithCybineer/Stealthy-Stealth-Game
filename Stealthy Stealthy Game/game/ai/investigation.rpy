

init python:

    def process_noise():

        for guard in guards:

            for sound in noise_events:

                dx = abs(guard.x - sound["x"])
                dy = abs(guard.y - sound["y"])

                if dx + dy < sound["volume"]:

                    guard.state = AIState.INVESTIGATE

        noise_events.clear()

        