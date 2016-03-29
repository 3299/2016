"""
Defines port numbers for motors and sensors.
"""

class Map(object):
    def __init__(self):
        # Joysticks have suffix 'J'
        self.leftJ       = 0
        self.middleJ     = 1
        self.rightJ      = 2

        # Motors have suffix 'M'. All motors use PWM.
        self.frontLeftM  = 8
        self.frontRightM = 9
        self.backLeftM   = 3
        self.backRightM  = 0

        self.beltM       = 7
        self.beltAxisM   = 2
        self.shootM      = 6
        self.flipM       = 4
        self.lift1M      = 1
        self.lift2M      = 5

        # lift and shoot are switched

        # Sensors have suffix 'S'. Gyro and sonar use analog in, everything else uses the DIO.
        self.gyroS       = 0
        self.sonarS      = 1
        self.beltAxisTS  = 0
        self.beltAxisBS  = 1
        self.flipS       = 2

        pass
