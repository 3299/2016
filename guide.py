"""
Guiding system for sonic sensor and vision.
"""

class Guiding(object):
    def __init__(self, sonic, chassis):
        self.sonic = sonic
        self.chassis = chassis

    def guideSonic(self):
        distance = self.sonic.getFeet()

        distance = distance - 5.5

        self.chassis.set(distance * 0.5, 0)
