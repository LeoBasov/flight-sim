"""
This module contains classes the represent the current kinetic state of the system.

"""

import numpy as np

class KineticState:
    def __init__(self):
        self.position = np.zeros(2)
        self.velocity = np.zeros(2)
