

init python:

    def update_guards():

        for guard in guards:

            if guard.state == AIState.PATROL:
                guard.patrol()

            elif guard.state == AIState.INVESTIGATE:
                guard.move_towards(
                    guard.last_noise_x,
                    guard.last_noise_y
                )

            elif guard.state == AIState.SEARCH:
                guard.search()

            elif guard.state == AIState.ALERT:
                guard.chase_player()

            elif guard.state == AIState.COMBAT:
                guard.attack()

                