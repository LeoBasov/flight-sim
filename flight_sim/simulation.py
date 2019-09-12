"""
Main module.

"""

class Simulation:
    def __init__(self):
        self.numeric_parameters = None
        self.plane = None

    def set_up(self, plane, numeric_parameters):
        self.plane = plane
        self.numeric_parameters = numeric_parameters

    def execute(self):
        pass

class NumericParameters:
    def __init__(self, dt = 1.0e-3):
        self.dt = dt
