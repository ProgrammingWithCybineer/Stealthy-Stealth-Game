

init python:

    class EliteGuard(Guard):

        def __init__(self, x, y):

            Guard.__init__(
                self,
                x,
                y,
                300
            )

            self.search_bonus = 2

            