"""
Main logic code
"""
import wpilib
import Map

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        # Mapping object stores port numbers for all connected motors, sensors, and joysticks. See map.py.
        Mapping = Map()

        # Init drivetrain
        self.robotDrive = wpilib.RobotDrive(Mapping.frontLeftM, Mapping.backLeftM, Mapping.frontRightM, Mapping.backRightM)
        self.robotDrive.setExpiration(0.1)

        # Init other motors
        self.beltM      = wpilib.Jaguar(Mapping.beltM)
        self.beltAxisM  = wpilib.Talon(Mapping.beltAxisM)
        # change to self.beltM = wpilib.Talon(Mapping.beltM) on comp bot
        self.shootM     = wpilib.Talon(Mapping.shootM)
        self.flipM      = wpilib.Jaguar(Mapping.flipM)
        self.liftM      = wpilib.Jaguar(Mapping.liftM)


        # Init joysticks
        self.leftJ      = wpilib.Joystick(Mapping.leftJ)
        self.middleJ    = wpilib.Joystick(Mapping.middleJ)
        self.rightJ     = wpilib.Joystick(Mapping.rightJ)

        # Init sensors
        self.sonar      = wpilib.AnalogInput(Mapping.sonar)

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        pass

    def testPeriodic(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
