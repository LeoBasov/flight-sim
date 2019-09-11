class Atmosphere:
    def __init__(self, H_0 = 0, p_0 = 101325, rho_0 = 1.225, T_0 = 288.15, H_i = 11000, p_i = 22632, rho_i = 0.3639, T_i = 216.65,):
        self.n = 1.235 #[-]
        self.R = 287.05 #[J / (kg K)]
        self.K = 1.405 #[-]
        self.g = 9.81 # [N kg^-1]

        self.H_0 = H_0 #[m]
        self.p_0 = p_0 #[N m^-2]
        self.rho_0 = rho_0 #[kg m^-3]
        self.T_0 = T_0 #[K]

        self.H_i = H_i
        self.p_i = p_i #[N m^-2]
        self.rho_i = rho_i #[kg m^-3]
        self.T_i = T_i #[K]

    def pressure(self, H):
        if H < self.H_i:
            return self.p_0*math.pow(self._inner_term_trhoposphere(H), (self.n/(self.n - 1.0)))
        else:
            return self.p_0*self._inner_term_stratosphere(H)

    def density(self, H):
        if H < self.H_i:
            return self.rho_0*math.pow(self._inner_term_trhoposphere(H), (1.0/(self.n - 1.0)))
        else:
            return self.rho_0*self._inner_term_stratosphere(H)

    def temperature(self, H):
        if H < self.H_i:
            return T_0*self._inner_term_trhoposphere(H)
        else:
            return self.T_i

    def speed_of_sound(self, H):
        return math.sqrt(self.K*self.R*self.temperature(H))

    def _inner_term_trhoposphere(self, H):
        return 1.0 - ((self.n - 1.0)/self.n)*(self.g/(self.R*self.T_0))*(H - self.H_0)

    def _inner_term_stratosphere(self, H):
        return math.exp(-self.g*(H - self.H_i)/(self.R*self.T_i))
