"""
Gets RMS-adjusted value in feet from the ultrasonic sensor.
"""

class Sonic(object):
    def __init__(self, sensor):
        self.sensor = sensor

    def getFeet(self):
        """
        loop = True
        distances = list()
        distances.extend([self.sensor.getValue()])

        while loop == True:
            if (len(distances) != 10):
                newDistance = self.sensor.getValue()
                if (distances[-1] != newDistance): # compare last taken value with new value
                    distances.extend([newDistance])
            else: # we're done!
                loop = False
        """
        distance = self.sensor.getValue()
        distance = (distance - 0.2) / 4.8

        distance = distance * 412
        #distance = distance / 100
        #distance = ((distance * 1000) / 4.883) * 2 # in cm
        #distance = distance * 0.0328084 # in feet

        return distance
