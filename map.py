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
        self.frontLeftM  = 3
        self.frontRightM = 6
        self.backLeftM   = 7
        self.backRightM  = 1

        self.beltM       = 9
        self.beltAxisM   = 0
        self.shootM      = 2
        self.flipM       = 5
        self.lift1M      = 4
        self.lift2M      = 8

        # Sensors have suffix 'S'. Gyro and sonar use analog in, everything else uses the DIO.
        self.gyroS       = 0
        #self.sonarS      = 1
        self.beltAxisTS  = 0
        self.beltAxisBS  = 1
        self.flipS       = 2
        self.sonicTrig   = 4
        self.sonicEcho   = 3

        pass
