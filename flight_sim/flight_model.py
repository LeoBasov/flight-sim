"""
The flight model is a 2D model for the flight profile.

"""

from .atmosphere import Atmosphere

class FlightModel:
    def __init__(self):
        self.angle_of_attack = 0.0
        self.height = 0.0

        self.atmospehere = Atmosphere()

    def thrust(self):
        return (0, 0)

    def drag(self):
        return (0, 0)

    def weight_force(self):
        return (0, 0)

    def lift(self):
        pass
