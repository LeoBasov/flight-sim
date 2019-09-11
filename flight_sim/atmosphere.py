class Atmosphere:
    def __init__(self, H_0 = 0, p_0 = 101325, rho_0 = 1.225, T_0 = 288.15, p_i = 22632, rho_i = 0.3639, T_i = 216.65,):
        self.n = 1.235 #[-]
        self.R = 287.05 #[J / (kg K)]
        self.K = 1.405 #[-]
        self.g = 9.81 # [N kg^-1]

        self.H_0 = H_0 #[m]

        self.p_0 = p_0 #[N m^-2]
        self.rho_0 = rho_0 #[kg m^-3]
        self.T_0 = T_0 #[K]

        self.p_i = p_i #[N m^-2]
        self.rho_i = rho_i #[kg m^-3]
        self.T_i = T_i #[K]

    def pressure(self, H):
        if H < 11000:
            return 0
        else:
            return 0

    def density(self, H):
        if H < 11000:
            return 0
        else:
            return 0

    def temperature(self, H):
        if H < 11000:
            return 0
        else:
            return 0

    def speed_of_sound(self, H):
        if H < 11000:
            return 0
        else:
            return 0
