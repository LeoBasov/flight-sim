"""
Describes the reaction of aerodynamical properties to the current state

"""

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
    def __init__(self):
        super().__init__()

    def drag_coefficient(self, kinetic_state):
        return 0.15

    def ref_area(self, kinetic_state):
        return 10.0
