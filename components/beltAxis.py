"""
Moves the belt up and down.
"""

class BeltAxis(object):
    def __init__(self, output):
        self.output = output

        self.direction = 1
        self.running = False

    def run(self, onV, stop1, stop2):
        if (stop1 == True or stop2 == True):
            self.running = False
            self.direction = self.direction * -1

        if (onV == True and self.running == False):
            self.running = True

        if (self.running == True):
            self.output.set(self.direction)

    def set(self, value):
        self.output.set(value)
