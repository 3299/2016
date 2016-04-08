"""
Main logic code
"""
import wpilib

from wpilib import SmartDashboard

from inits import Component
from helpers import help
from components.vision import Vision

from components.chassis import Chassis
from components.belt import Belt
from components.beltAxis import BeltAxis
from components.shooter import Shooter
from components.lift import Lift
from components.sonic import Sonic
from components.arduino import Arduino
from guide import Guiding

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See components.py.

        # Setup subsystems
        self.drive    = Chassis(self.C.driveTrain, self.C.gyroS)
        self.belt     = Belt(self.C.beltM)
        self.beltAxis = BeltAxis(self.C.beltAxisM)
        self.shoot    = Shooter(self.C.flipM, self.C.shootM)
        self.lift     = Lift(self.C.lift1M, self.C.lift2M)
        self.sonic    = Sonic(self.C.sonic)
        self.arduino  = Arduino(self.C.arduino)

        self.guide    = Guiding(self.sonic, self.drive)

        self.sd = SmartDashboard
        self.sd.putBoolean("autoMove", False)

        self.autoLoop = 0

    def operatorControl(self):
        self.C.driveTrain.setSafetyEnabled(True) # keeps robot from going crazy if connection with DS is lost

        while self.isOperatorControl() and self.isEnabled():
            distance = self.sonic.getAverage()
            print(distance)
            self.sd.putDouble('distance', distance)

            if (5.25 < distance and distance < 5.75):
                self.sd.putBoolean("Ready", True)
            else:
                self.sd.putBoolean("Ready", False)

            if (self.C.middleJ.getRawButton(1) == True):
                self.guide.guideSonic()

            # Drive
            self.drive.run(self.C.leftJ.getRawButton(1), self.C.leftJ.getY(), self.C.middleJ.getY())

            # Components
            self.belt.run(self.C.rightJ.getRawButton(4), self.C.rightJ.getRawButton(5))
            self.beltAxis.run(self.C.rightJ.getRawButton(3), self.C.rightJ.getY(), self.C.beltAxisTS.get(), self.C.beltAxisBS.get())
            self.lift.run(self.C.leftJ.getRawButton(1), self.C.leftJ.getY(), self.C.middleJ.getY())
            self.shoot.run(self.C.rightJ.getRawButton(2), self.C.beltAxisTS.get(), self.C.rightJ.getRawButton(1), self.C.flipS.get()) # weird argument in the middle makes sure shooter doesn't turn on when belt it up

            wpilib.Timer.delay(0.005) # wait for a motor update time

    def autonomous(self):
        """This function is called periodically during autonomous."""
        if (self.sd.getBoolean("autoMove") == True):
            distance = self.sonic.getAverage()

            while (self.autoLoop < 2000 and distance > 5):
                self.drive.set(-1, 0)
                wpilib.Timer.delay(0.005)
                self.autoLoop = self.autoLoop + 1


    def test(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
