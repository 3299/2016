"""
Main logic code
"""
import wpilib
from components import Component
from vision import Vision
from limit import Limit
from triggerRun import triggerRun

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See components.py.
        self.vision = Vision()

        # Defines triggers for motors
        self.beltRun = triggerRun(self.C.irightJ().getRawButton(2), self.C.beltM)
        self.beltAxisLimit = Limit(self.C.irightJ().getRawButton(3), self.C.beltAxisM, self.C.beltAxisBS.get(), self.C.beltAxisTS.get())

    def operatorControl(self):
        self.C.driveTrain.setSafetyEnabled(True) # keeps robot from going crazy if connection with DS is lost

        while self.isOperatorControl() and self.isEnabled():
            # Drive
            self.C.driveTrain.tankDrive(self.C.ileftJ(), self.C.imiddleJ())

            # All the triggers for these are defined in robotInit
            self.beltRun.run()
            self.beltAxisLimit.run()

            wpilib.Timer.delay(0.005) # wait for a motor update time

    def autonomous(self):
        """This function is called periodically during autonomous."""
        pass

    def test(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
