"""
Describes the reaction of aerodynamical properties to the current state

"""

import math

class Aero:
    def __init__(self):
        pass

    def lift_coefficient(self, kinetic_state):
        return 0.0

    def drag_coefficient(self, kinetic_state):
        return 0.0

    def ref_area(self, kinetic_state):
        return 0.0

class Simple(Aero):
    def __init__(self, ref_radius, ref_length, ref_drag_area, wetted_area):
        super().__init__()
        self.atmosphere = 0

        self.ref_radius = ref_radius
        self.ref_length = ref_length
        self.ref_drag_area = ref_drag_area
        self.wetted_area = wetted_area

        self.cd_wave = self.calc_cd_wave(self.ref_radius, self.ref_length)

    def drag_coefficient(self, kinetic_state):
        sw_to_sref = 0
        cf = 0

        return 0.167

    def calc_cd_wave(self, ref_radius, ref_length):
        return 4.0*math.pi*math.pi*ref_radius*ref_radius/(ref_length*ref_length)

    def ref_area(self, kinetic_state):
        return 10.0
