"""
Describes the reaction of aerodynamical properties to the current state

"""

class Aero:
    def __init__(self):
        pass

    def get_lift_coefficient(self, kinetic_state):
        return 0.0

    def get_drag_coefficient(self, kinetic_state):
        return 0.0

class Simple(Aero):
    def __init__(self):
        super().__init__()

    def get_drag_coefficient(self, kinetic_state):
        return 0.05
