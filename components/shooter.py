"""
Controls both the shooting wheels and the flipper.
"""

class Shooter(object):
    # trigger is boolean, output is a motor controller
    def __init__(self, flipO, shootO):
        self.flipO  = flipO
        self.shootO = shootO

        self.shootOn = False
        self.flipOn  = False

    def run(self, shootV, flipV, stop1):
        if (flipV == True and self.flipOn == False):
            self.flipOn = True

        if (shootV == True and self.shootOn == False):
            self.shootOn = True

        if (self.shootOn == True):
            self.shootO.set(1)

        if (self.flipOn == True):
            self.flipO.set(1)

        if (self.flipOn == True and stop1 == True):
            self.shootOn = False
            self.flipOn  = False
