"""
The flight model is a 2D model for the flight profile.

"""

import numpy as np
from .atmosphere import Atmosphere

class FlightModel:
    def __init__(self, fuel_mass):
        self.angle_of_attack = 0.0
        self.position = np.zeros(2)
        self.velocity = np.zeros(2)

        self.atmospehere = Atmosphere()

        self.fuel_fraction = 2.0/3.0

        self.fuel_mass = fuel_mass
        self.dry_mass = (self.fuel_mass/self.fuel_fraction) - self.fuel_mass

        self.mass_flow = 50 #[kg/s]

    def total_mass(self):
        return self.fuel_mass + self.dry_mass

    def thrust(self):
        return np.zeros(2)

    def drag(self):
        return np.zeros(2)

    def weight_force(self):
        return np.zeros(2)

    def lift(self):
        return np.zeros(2)

    def process(self, dt):
        self.fuel_mass -= dt*self.mass_flow
