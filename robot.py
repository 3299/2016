"""
Main logic code
"""
import wpilib
from components import Component
from vision import Vision
from limit import Limit
from trigger import trigger
from drive import DriveTrain

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See components.py.
        self.vision = Vision()

        # Setup motors
        self.drive = DriveTrain(self.C.driveTrain, self.C.gyroS)
        self.belt = trigger(self.C.rightJ.getRawButton(2), self.C.beltM)
        self.beltAxisLimit = Limit(self.C.rightJ.getRawButton(3), self.C.beltAxisM, self.C.beltAxisBS.get(), self.C.beltAxisTS.get())
        self.flip = Limit(self.C.rightJ.getRawButton(4), self.C.flipM, self.C.flipS.get(), self.C.flipS.get())
        self.shoot = trigger(self.C.rightJ.getTrigger(), self.C.shootM)

    def operatorControl(self):
        self.C.driveTrain.setSafetyEnabled(True) # keeps robot from going crazy if connection with DS is lost

        while self.isOperatorControl() and self.isEnabled():
            # Drive
            self.C.driveTrain.tankDrive(self.C.leftJ, self.C.middleJ)

            # All the triggers for these are defined in robotInit
            self.drive.run(self.C.leftJ.getY(), self.C.middleJ.getY())
            self.belt.run()
            self.beltAxisLimit.run()
            self.flip.run()
            self.shoot.run()

            wpilib.Timer.delay(0.005) # wait for a motor update time

    def autonomous(self):
        """This function is called periodically during autonomous."""
        pass

    def test(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
