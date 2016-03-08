"""
Main logic code
"""
import wpilib
from components import Component
from vision import Vision
from limit import Limit

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See components.py.
        self.vision = Vision()
        self.beltLimit = Limit(self.C.irightJ.getButton(1), self.C.beltM, self.C.beltAxisBS.get(), self.C.beltAxisTS.get())

    def operatorControl(self):
        self.C.driveTrain.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            # Drive
            self.C.driveTrain.tankDrive(self.C.ileftJ(), self.C.imiddleJ())

            # When button 2 on right joystick is held down the belt runs
            if (self.C.irightJ.getButton(2) == True):
                self.beltM.set(1)
            else:
                self.beltM.set(0)

            self.beltLimit.run()

            wpilib.Timer.delay(0.005) # wait for a motor update time

    def autonomous(self):
        """This function is called periodically during autonomous."""
        pass

    def test(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
