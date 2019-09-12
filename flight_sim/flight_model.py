"""
The flight model is a 2D model for the flight profile.

"""

from .atmosphere import Atmosphere

class FlightModel:
    def __init__(self, fuel_mass):
        self.angle_of_attack = 0.0
        self.height = 0.0

        self.atmospehere = Atmosphere()

        self.fuel_fraction = 2.0/3.0

        self.fuel_mass = fuel_mass
        self.dry_mass = (self.fuel_mass/self.fuel_fraction) - self.fuel_mass

    def total_mass(self):
        return self.fuel_mass + self.dry_mass

    def thrust(self):
        return (0, 0)

    def drag(self):
        return (0, 0)

    def weight_force(self):
        return (0, 0)

    def lift(self):
        pass
