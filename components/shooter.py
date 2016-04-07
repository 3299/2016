"""
Controls both the shooting wheels and the flipper.
"""

class Shooter(object):
    # trigger is boolean, output is a motor controller
    def __init__(self, flipO, shootO):
        self.flipO  = flipO
        self.shootO = shootO

        self.flipOn = False

    def run(self, on, limit1, shoot, stop1):
        if (stop1 != False or self.flipOn == True):
            self.flipO.set(0.75)
        else:
            self.flipO.set(0)

        if (shoot == True):
            self.flipOn = True

        if (stop1 == False):
            self.flipOn = False
