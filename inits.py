"""
Inits wpilib objects
"""

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
        self.beltM      = wpilib.Talon(Mapping.beltM)
        self.beltAxisM  = wpilib.Jaguar(Mapping.beltAxisM)
        self.shootM     = wpilib.Talon(Mapping.shootM)
        self.flipM      = wpilib.Jaguar(Mapping.flipM)
        self.lift1M     = wpilib.Talon(Mapping.lift1M)
        self.lift2M     = wpilib.Talon(Mapping.lift2M)

        # Init joysticks
        self.leftJ      = wpilib.Joystick(Mapping.leftJ)
        self.middleJ    = wpilib.Joystick(Mapping.middleJ)
        self.rightJ     = wpilib.Joystick(Mapping.rightJ)

        # Init sensors
        self.gyroS      = wpilib.AnalogGyro(Mapping.gyroS)
        self.sonic      = wpilib.Ultrasonic(Mapping.sonicTrig, Mapping.sonicEcho)
        self.beltAxisTS = wpilib.DigitalInput(Mapping.beltAxisTS)
        self.beltAxisBS = wpilib.DigitalInput(Mapping.beltAxisBS)
        self.flipS      = wpilib.DigitalInput(Mapping.flipS)

        # Init I2C for communication with Arduino
        self.arduino    = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4)
