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

    def run(self, on, off, shoot, stop1):
        if (self.shootOn == True):
            self.shootO.set(1)
        else:
            self.shootO.set(0)

        if (self.triggerPulled == True and stop1 == False):
            self.flipOn = True

        if (self.flipOn == True):
            self.flipO.set(0.25)
        else:
            self.flipO.set(0)

        if (stop1 == False):
            self.flipOn = False


        # Triggers
        if (on == True):
            self.shootOn = True
        if (off == True):
            self.shootOn = False
        """
        if (stop1 == True):
            self.flipOn = True
            self.triggerPulled = False
        """
        if (shoot == True):
            self.triggerPulled = True
            self.flipOn = True
