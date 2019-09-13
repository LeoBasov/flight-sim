"""
Solver module.

"""

import numpy as np

class Aero:
    def __init__(self):
        pass

    def execute(self, plane):
        pass

class Flight:
    def __init__(self):
        pass

    def execute(self, plane):
        pass

class Kinetic:
    def __init__(self):
        pass

    def execute(self, plane, dt):
        self.calc_gravitational_force(plane)

        accleration = plane.kinetic_state.total_force/plane.total_mass()

        plane.kinetic_state.position += plane.kinetic_state.velocity*dt + 0.5*accleration*dt*dt
        plane.kinetic_state.velocity += accleration*dt

        plane.kinetic_state.total_force = np.zeros(2)

    def calc_gravitational_force(self, plane):
        force = np.zeros(2)
        force[1] = -9.81*plane.total_mass()

        plane.kinetic_state.total_force += force
