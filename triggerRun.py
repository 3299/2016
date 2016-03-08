"""
Turns motor on when trigger is true
"""

class triggerRun(object):
    # trigger is boolean, output is a motor controller
    def __init__(self, trigger, output):
        self.trigger = trigger
        self.output  = output

    def run(self):
        if (self.trigger == True):
            self.output.set(1)
        else:
            self.output.set(0)
