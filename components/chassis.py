"""
Drives. Can accept input from joysticks or values [-1, 1]. Uses the gyro for better steering.
"""

class Chassis(object):
    def __init__(self, drive, gyro):
        self.drive = drive
        self.gyro  = gyro

        self.Kp    = 0.03

    def run(self, on, leftP, rightP):
        """turning = leftP - rightP
        turning = turning * 0.5
        power = abs(leftP) + abs(rightP)

        turning = turning - (self.gyro.getAngle() * self.Kp)

        self.drive.drive(power, turning)
        #self.drive.tankDrive(leftP, rightP)
        """
        if (on != True):
            self.drive.tankDrive(leftP, rightP)

    def set(self, power, turning):
        self.drive.drive(power, turning)
