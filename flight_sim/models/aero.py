"""
Describes the reaction of aerodynamical properties to the current state

"""

import math
import numpy as np
from . import atmosphere

class Aero:
    def __init__(self):
        pass

    def lift_coefficient(self, kinetic_state):
        return 0.0

    def drag_coefficient(self, kinetic_state):
        return 0.0

class Simple(Aero):
    def __init__(self, ref_radius, ref_length, ref_drag_area, wetted_area):
        super().__init__()
        self.atmosphere = atmosphere.Atmosphere()

        self.ref_radius = ref_radius
        self.ref_length = ref_length
        self.ref_drag_area = ref_drag_area
        self.wetted_area = wetted_area

        self.cd_wave = self.calc_cd_wave(self.ref_radius, self.ref_length)

    def drag_coefficient(self, kinetic_state):
        sw_to_sref = self.wetted_area/self.ref_drag_area
        mach_number = np.linalg.norm(kinetic_state.velocity) / self.atmosphere.speed_of_sound(kinetic_state.position[1])

        if mach_number > 0.3:
            cf = self.calc_cf(mach_number, self.ref_length)
            cd = cf*sw_to_sref + self.cd_wave
        else:
            cd = 0.167

        return cd

    def calc_cd_wave(self, ref_radius, ref_length):
        #return 4.0*math.pi*math.pi*ref_radius*ref_radius/(ref_length*ref_length) formula is wrong

        return 0.1538

    def calc_cf(self, mach_number, ref_length):
        k_factor = 0.7e-5 #for smooth modlede composites
        Re_cutoff = self.clac_Re_cutoff(mach_number, ref_length, k_factor)

        return 0.455/(math.pow(math.log(Re_cutoff), 2.58)*math.pow(1.0 + 0.144*mach_number*mach_number, 0.65))

    def clac_Re_cutoff(self, mach_number, ref_length, k_factor):
        return math.pow(ref_length/k_factor, 1.053)*math.pow(mach_number, 1.16)
