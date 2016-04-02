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
        self.triggerPulled = False

    def run(self, on, limit1, shoot, stop1):
        if (limit1 == False):
            self.shootOn = False

        if (self.shootOn == True):
            self.shootO.set(1)
        else:
            self.shootO.set(0)

        if (self.triggerPulled == True and stop1 == False):
            self.flipOn = True
            self.shootOn = False

        if (self.flipOn == True):
            self.flipO.set(0.25)
        else:
            self.flipO.set(0)

        if (stop1 == False):
            self.flipOn = False


        # Triggers
        if (on == True and limit1 == True):
            self.shootOn = True
        if (shoot == True):
            self.triggerPulled = True
            self.flipOn = True
