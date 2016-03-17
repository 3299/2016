"""
Runs the belt.
"""

class Belt(object):
    def __init__(self, output):
        self.output = output

    def run(self, onV):
        if (onV == True):
            self.output.set(1)
        else:
            self.output.set(0)

    def set(self, value):
        self.output.set(value)
