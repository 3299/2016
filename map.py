"""
Defines port numbers for motors and sensors.
"""

class Map(object):
    def __init__(self):
        # Joysticks have suffix 'J'
        self.leftJ       = 0
        self.middleJ     = 1
        self.rightJ      = 2

        # Maps for buttons-to-actions have suffix 'BA'


        # Motors have suffix 'M'
        self.frontLeftM  = 5
        self.frontRightM = 4
        self.backLeftM   = 3
        self.backRightM  = 0

        self.beltM       = 8
        self.beltAxisM   = 6
        self.shootM      = 7
        self.flipM       = 9
        self.liftM       = 1

        # Sensors
        self.sonar       = 0
        
        pass
