"""
Controls both the shooting wheels and the flipper.
"""

class Shooter(object):
    # trigger is boolean, output is a motor controller
    def __init__(self, flipO, shootO):
        self.flipO  = flipO
        self.shootO = shootO

        self.flipOn = False
        self.running = False
        self.ableToStop = False

    def run(self, shooterB, topLimit, flipB, hallEffectS):

        if(shooterB == True):
            self.shootO.set(1)
            self.ableToStop = False

        if(flipB == True):
            self.ableToStop = False
            self.flipO.set(0.75)

        if(hallEffectS == True):
            self.ableToStop = True

        if(self.ableToStop == True and hallEffectS == False):
            self.flipO.set(0)
            self.shootO.set(0)

        """
        if (on == True):
            self.running = True

        if (self.running == True):
            self.shootO.set(1)
        else:
            self.shootO.set(0)

        if (stop1 == True or self.flipOn == True):
            self.flipO.set(0.75)
        else:
            self.flipO.set(0)
            self.flipOn = False

        if (stop1 == False):
            self.flipOn = False


        if (shoot == True):
            self.flipOn = True
        """
