"""
This module contains classes the represent the current kinetic state of the system.

"""

import math
from . import kinetic

class Plane:
    def __init__(self):
        self.aero_model = None
        self.engine_model = None
        self.flight_model = None
        self.kinetic_state = kinetic.KineticState()

        self.dry_mass = None
        self.fuel_mass = None

    def total_mass(self):
        return self.dry_mass + self.fuel_mass

    def fire_engine(self, dt):
        if self.fuel_mass > 0.0:
            burned_fuel = self.engine_model.mass_flow*dt
            thrust = self.engine_model.thrust(self.kinetic_state.position, self.kinetic_state.velocity)
            self.kinetic_state.total_force[0] += thrust*math.cos(self.kinetic_state.angle)
            self.kinetic_state.total_force[1] += thrust*math.sin(self.kinetic_state.angle)

            if burned_fuel <= self.fuel_mass:
                self.fuel_mass -= burned_fuel    
            else:
                self.fuel_mass = 0.0
