"""
Main logic code
"""
import wpilib
from inits import Component
from components.vision import Vision

from components.chassis import Chassis
from components.belt import Belt
from components.beltAxis import BeltAxis
from components.shooter import Shooter

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See components.py.
        self.vision = Vision()

        # Setup subsystems
        self.drive    = Chassis(self.C.driveTrain, self.C.gyroS)
        self.belt     = Belt(self.C.beltM)
        self.beltAxis = BeltAxis(self.C.beltAxisM)
        self.shoot    = Shooter(self.C.flipM, self.C.shootM)

    def operatorControl(self):
        self.C.driveTrain.setSafetyEnabled(True) # keeps robot from going crazy if connection with DS is lost

        while self.isOperatorControl() and self.isEnabled():
            # Drive
            self.C.driveTrain.tankDrive(self.C.leftJ, self.C.middleJ)

            self.drive.run(self.C.leftJ.getY(), self.C.middleJ.getY())
            self.belt.run(self.C.rightJ.getRawButton(2))
            self.beltAxis.run(self.C.rightJ.getRawButton(3), self.C.beltAxisBS.get(), self.C.beltAxisTS.get())
            self.shoot.run(self.C.rightJ.getRawButton(5), self.C.rightJ.getRawButton(1), self.C.flipS.get())

            wpilib.Timer.delay(0.005) # wait for a motor update time

    def autonomous(self):
        """This function is called periodically during autonomous."""
        pass

    def test(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
