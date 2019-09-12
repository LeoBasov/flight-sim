"""
The flight model is a 2D model for the flight profile.

"""

import numpy as np
import math
from .atmosphere import Atmosphere

class FlightModel:
    def __init__(self, fuel_mass):
        self.angle_of_attack = 0.5*math.pi
        self.position = np.zeros(2)
        self.velocity = np.zeros(2)

        self.atmospehere = Atmosphere()

        self.fuel_fraction = 2.0/3.0

        self.fuel_mass = fuel_mass
        self.dry_mass = (self.fuel_mass/self.fuel_fraction) - self.fuel_mass

        self.mass_flow = 25 #[kg/s]
        self.exit_velocity = 1800 #[m/s]

    def total_mass(self):
        return self.fuel_mass + self.dry_mass

    def thrust(self):
        if self.fuel_mass > 0:
            thrust_loc = self.mass_flow*self.exit_velocity
        else:
            thrust_loc = 0

        return np.array([math.cos(self.angle_of_attack)*thrust_loc, math.sin(self.angle_of_attack)*thrust_loc])

    def drag(self):
        return np.zeros(2)

    def weight_force(self):
        return np.array([0, -9.81*self.total_mass()])

    def lift(self):
        return np.zeros(2)

    def process(self, dt):
        self.fuel_mass -= dt*self.mass_flow
