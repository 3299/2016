"""
Controls both the shooting wheels and the flipper.
"""

class Shooter(object):
    # trigger is boolean, output is a motor controller
    def __init__(self, flipO, shootO):
        self.flipO  = flipO
        self.shootO = shootO

        self.ableToStop = False

    def run(self, shooterB, topLimit, flipB, hallEffectS):
        if (shooterB == True):
            self.shootO.set(1)
            self.ableToStop = False

        if (flipB == True):
            self.ableToStop = False
            self.flipO.set(0.75)

        if (hallEffectS == True):
            self.ableToStop = True

        if (self.ableToStop == True and hallEffectS == False):
            self.flipO.set(0)
            self.shootO.set(0)
