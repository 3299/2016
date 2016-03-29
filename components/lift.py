"""
Lifter
"""

class Lift(object):
    def __init__(self, output1, output2):
        self.output1 = output1
        self.output2 = output2

    def run(self, trigger, stage1, stage2):
        if (trigger == True):
            self.output1.set(stage1)
            self.output2.set(stage2)
        else:
            self.output1.set(0)
            self.output2.set(0)
