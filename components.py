import wpilib
from map import Map

class Component(object):
    def __init__(self):
        # Mapping object stores port numbers for all connected motors, sensors, and joysticks. See map.py.
        Mapping = Map()

        # Init drivetrain
        self.driveTrain = wpilib.RobotDrive(Mapping.frontLeftM, Mapping.backLeftM, Mapping.frontRightM, Mapping.backRightM)
        self.driveTrain.setExpiration(0.1)

        # Init other motors
        self.beltM      = wpilib.Jaguar(Mapping.beltM)
        # change to self.beltM = wpilib.Talon(Mapping.beltM) on comp bot
        self.beltAxisM  = wpilib.Talon(Mapping.beltAxisM)
        self.shootM     = wpilib.Talon(Mapping.shootM)
        self.flipM      = wpilib.Jaguar(Mapping.flipM)
        self.liftM      = wpilib.Jaguar(Mapping.liftM)
        # change to liftM = wpilib.Talon(Mapping.liftM)

        # Init joysticks
        self.leftJ      = wpilib.Joystick(Mapping.leftJ)
        self.middleJ    = wpilib.Joystick(Mapping.middleJ)
        self.rightJ     = wpilib.Joystick(Mapping.rightJ)

        # Init sensors
        self.sonarS     = wpilib.AnalogInput(Mapping.sonarS)
        self.beltAxisTS = wpilib.DigitalInput(Mapping.beltAxisTS)
        self.beltAxisBS = wpilib.DigitalInput(Mapping.beltAxisBS)

    def ileftJ(self):
        return self.leftJ
    def imiddleJ(self):
        return self.middleJ
    def irightJ(self):
        return self.rightJ
