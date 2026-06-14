

init python:

    noise_events = []

    def generate_noise(x, y, volume):

        noise_events.append({
            "x": x,
            "y": y,
            "volume": volume
        })

        