class Limit(object):
    # Trigger is boolean, output is a motor controller, stop1 and stop2 are boolean
    def __init__(self, trigger, output, stop1, stop2):
        self.trigger = trigger
        self.output  = output
        self.stop1   = stop1
        self.stop2   = stop2

        self.direction = -1
        self.running = False

    def run(self):
        if (self.trigger == True):
            # set direction
            if (self.stop1 == True):
                self.direction = -1
            else if (self.stop2 == True):
                self.direction = 1

            self.output.set(self.direction)
            self.running = True # set to true so that bottem if will run on next iteration

        if (self.stop1 == True || self.stop2 == True):
            self.output.set(0) # stop the motor
            self.running = False
            self.direction = self.direction * -1 # next time this is triggered it needs to run the other way

        if (self.running == True):
            self.output.set(self.direction)
