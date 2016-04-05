"""
Helper class for ultrasonic sensor
"""

class Sonic(object):
    def __init__(self, sensor):
        self.sensor = sensor
        self.sensor.setAutomaticMode(True)

    def getFeet(self):
        distance = self.sensor.getRangeInches()
        distance = distance / 12

        return distance
