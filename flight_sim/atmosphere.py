class Atmosphere:
    def __init__(self, p_0 = 101325, rho_0 = 1.225, T_0 = 288.15, p_i = 22632, rho_i = 0.3639, T_i = 216.65,):
        self.n = 1.235 #[-]
        self.R = 287.05 #[J / (kg K)]
        self.K = 1.405 #[-]
        self.g = 9.81 # [N kg^-1]

        self.p_0 = p_0 #[N m^-2]
        self.rho_0 = rho_0 #[kg m^-3]
        self.T_0 = T_0 #[K]

        self.p_i = p_i #[N m^-2]
        self.rho_i = rho_i #[kg m^-3]
        self.T_i = T_i #[K]
