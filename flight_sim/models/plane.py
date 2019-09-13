"""
This module contains classes the represent the current kinetic state of the system.

"""

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
            self.fuel_mass -= self.engine_model.mass_flow*dt
            self.kinetic_state.total_force += self.engine_model.thrust(self.kinetic_state.position, self.kinetic_state.velocity)
