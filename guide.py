"""
Guiding system for sonic sensor and vision.
"""

class Guiding(object):
    def __init__(self, sonic, vision, chassis):
        self.sonic = sonic
        self.vision = vision
        self.chassis = chassis

    def guideSonic(self):
        """
        if (forward == True):
            self.output.set(-1)
            self.arduino.send(color + "f")
        elif (backward == True):
            self.output.set(1)
            self.arduino.send(color + "z")
        else:
            self.output.set(0)
        """

    def guideVision(self):
        turn = self.vision.getTurn()
        if (turn != False):
            print(turn)
            self.chassis.set(1, turn)
