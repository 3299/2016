"""
Main logic code
"""
import wpilib
from components import Component
from vision import Vision

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See components.py.
        self.vision = Vision()

    def operatorControl(self):
        self.C.driveTrain.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            self.C.driveTrain.tankDrive(self.C.leftJ, self.C.middleJ)

            if (self.C.leftJ.getTrigger()):
                print(self.vision.getData())

            wpilib.Timer.delay(0.005) # wait for a motor update time

    def autonomous(self):
        """This function is called periodically during autonomous."""
        pass

    def test(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
