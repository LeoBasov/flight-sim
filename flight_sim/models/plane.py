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
