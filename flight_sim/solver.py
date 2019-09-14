"""
Solver module.

"""

import math
import numpy as np
from .models.atmosphere import Atmosphere

class Aero:
    def __init__(self):
        self.atmosphere = Atmosphere()

    def execute(self, plane, dt):
        ref_area = plane.aero_model.ref_area(plane.kinetic_state)
        velocity = np.linalg.norm(plane.kinetic_state.velocity)
        rho = self.atmosphere.density(plane.kinetic_state.position[1])
        lift = np.zeros(2)
        drag = np.zeros(2)
        c_l = plane.aero_model.lift_coefficient(plane.kinetic_state)
        c_d = plane.aero_model.drag_coefficient(plane.kinetic_state)

        if velocity > 0:
            flight_vec = plane.kinetic_state.velocity/velocity
        else:
            flight_vec = np.zeros(2)

        lift[0] = 0.5*c_l*rho*velocity*velocity*ref_area*math.cos(plane.kinetic_state.angle)
        lift[1] = 0.5*c_l*rho*velocity*velocity*ref_area*math.sin(plane.kinetic_state.angle)

        drag = -1.0*0.5*c_d*rho*velocity*velocity*ref_area*flight_vec

        plane.kinetic_state.total_force += lift + drag

class Flight:
    def __init__(self):
        pass

    def execute(self, plane, dt):
        plane.fire_engine(dt)

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
