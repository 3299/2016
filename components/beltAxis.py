"""
Moves the belt up and down.
"""

class BeltAxis(object):
    def __init__(self, output):
        self.output = output

        self.direction = 1
        self.running = False

    def run(self, on, value, stop1, stop2):
        # stop1 is top switch, stop2 is bottom stop1 = True?
        """
        if (stop1 == False or stop2 == False):
            self.running = False
            self.direction = self.direction * -1

        if (onV == True and self.running == False):
            self.running = True

        if (self.running == True):
            self.output.set(self.direction)
        """
        if (on == True):
            if (stop2 == False and value < 0):
                self.output.set(0)
            elif (stop1 == False and value > 0):
                self.output.set(0)
            else:
                self.output.set(value)
        else:
            self.output.set(0)

    def set(self, value):
        self.output.set(value)
