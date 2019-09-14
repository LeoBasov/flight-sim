"""
Describes the reaction of engine properties to the current state

"""

from .atmosphere import Atmosphere

class Engine:
    def __init__(self):
        pass

    def thrust(self, height, velocity):
        return 0.0

class JP5_H2O2(Engine):
    def __init__(self, mass_flow):
        super().__init__()
        self.ce_ground = 2530.98 #3168.63 whute paper
        self.ce_vacuum = 2632.2192 #3286.35
        self.mass_flow = mass_flow
        self.atmosphere = Atmosphere()

    def get_ce(self, position):
        rho = self.atmosphere.density(position[1])
        frac = rho/self.atmosphere.rho_0

        return self.ce_vacuum*(1.0 - frac) + self.ce_ground*frac

    def thrust(self, position, velocity):
        return self.get_ce(position)*self.mass_flow

class HTPB_N2O(Engine):
    def __init__(self, mass_flow):
        super().__init__()
        self.ce_ground = 2423.07 #3168.63 whute paper
        self.ce_vacuum = 2519.99 #3286.35
        self.mass_flow = mass_flow
        self.atmosphere = Atmosphere()

    def get_ce(self, position):
        rho = self.atmosphere.density(position[1])
        frac = rho/self.atmosphere.rho_0

        return self.ce_vacuum*(1.0 - frac) + self.ce_ground*frac

    def thrust(self, position, velocity):
        return self.get_ce(position)*self.mass_flow
