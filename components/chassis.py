"""
Drives. Can accept input from joysticks or values [-1, 1]. Uses the gyro for better steering.
"""

class Chassis(object):
    def __init__(self, drive, gyro):
        self.drive = drive
        self.gyro  = gyro

        self.Kp    = 0.03

    def run(self, leftP, rightP):
        """
        average = leftP + rightP
        average = average / 2

        turning = (average - self.gyro.getAngle()) * self.Kp

        self.drive.drive(average, turning)
        """
        self.drive.tankDrive(leftP, rightP)

    def set(self, power, turning):
        self.drive.drive(power, turning)
