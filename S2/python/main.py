import numpy as np
import matplotlib.pyplot as plt

import kinetic_dimless as solver
from atmosphere import Atmosphere

atm = Atmosphere()

def plot_x(sol, params):
    plt.plot(sol.t / params.t_meco, sol.y[0] * params.x_ref / 100000.0)
    plt.axhline(y=1, color="black", linestyle="--")
    plt.axvline(x=1, color="black", linestyle="--")
    plt.xlabel("$t$ / $t_{\mathrm{MECO}}$")
    plt.ylabel("$x$ / $x_{\mathrm{Karman}}$")
    plt.show()

def plot_dot_x(sol, params):
    Ma = []
    
    for i in range(len(sol.t)):
        H = sol.y[0][i] * params.x_ref
        Ma.append(sol.y[1][i] * params.c0 / atm.speed_of_sound(H))
    
    plt.plot(sol.t / params.t_meco, sol.y[1])
    plt.plot(sol.t / params.t_meco, Ma, "-.")
    plt.axhline(y=1, color="black", linestyle="--")
    plt.axvline(x=1, color="black", linestyle="--")
    plt.xlabel("$t$ / $t_{\mathrm{MECO}}$")
    plt.ylabel("$\mathrm{Ma}$")
    plt.legend(["$\dot{x}/\sqrt{\gamma R T_0}$", "$\dot{x}/\sqrt{\gamma R T(x)}$"])
    plt.show()

if __name__ == '__main__':
    params = solver.Parameters()
    
    t = np.linspace(0, 10)
    y0 = (0.0, 0.0)
    
    params.T = 2.0
    params.Ma_ce = 2800.0 / atm.speed_of_sound(0.0)
    params.Ma_L = 100.0 / atm.speed_of_sound(0.0)
    params.CD = 0.025 # subsonic
    params.CA_L = 1.5
    params.mf = 0.5
    
    sol = solver.solve_trajectory(t, y0, params)
    
    plot_dot_x(sol, params)
    plot_x(sol, params)
    
    print("done")