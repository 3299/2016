"""
Moves the ball flipper so that the ball is moved from the belt to the shooting motors.
"""

from datetime import datetime

class Flip(object):
    # Trigger is boolean, output is a motor controller, stop1 and stop2 are boolean
    def __init__(self, joystick, button, output, stop1):
        self.joystick  = joystick
        self.button    = button
        self.output    = output
        self.stop1     = stop1

        self.direction = -0.25
        self.running   = False

        self.state = False
        self.lastState = False
        self.lastDebounceTime = 0

    def run(self):
        #Debounce
        self.reading = self.stop1.get()

        if (self.reading != self.lastState):
            self.debounceTime = datetime.now()
            self.debounceTime = self.debounceTime.microsecond

        self.now = datetime.now()
        self.now = self.now.microsecond

        if ((self.now - self.lastDebounceTime) > 75):
            if (self.reading != self.state):
                self.state = self.reading

        self.lastState = self.reading

        #Logic
        print(self.state)
        if (self.running == True):
            self.output.set(0.25)

        if (self.state == True):
            self.running = False
            self.output.set(0)

        if (self.joystick.getRawButton(self.button) == True):
            self.running = True

        """
        if (self.state == True):
            self.output.set(0) # stop the motor
            self.running = False
            self.direction = self.direction * -1 # next time this is triggered it needs to run the other way

        if (self.running == True):
            self.output.set(self.direction)

        if (self.joystick.getRawButton(self.button) == True):
            # set direction
            if (self.stop1.get() == True):
                self.direction = -0.25
            else:
                self.direction = 0.25

            self.output.set(self.direction)
            self.running = True # set to true so that bottem if will run on next iteration
        """
