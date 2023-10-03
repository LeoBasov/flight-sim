import numpy as np
from scipy.integrate import solve_ivp
from scipy import constants as cst

from atmosphere import Atmosphere

atm = Atmosphere()
g = cst.g
c0 = atm.speed_of_sound(0.0)

rho_ref = atm.density(0.0)
t_ref = c0/g
ddot_x_ref = g
dot_x_ref = ddot_x_ref*t_ref
x_ref = dot_x_ref*t_ref

class Parameters:
    def __init__(self):
        self.T = 1.0
        self.Ma_ce = 2.0
        self.Ma_L = 0.3
        self.CD = 0.1
        self.CA_L = 0.1
        self.mf = 0.5
        
        self.set_up()
        
    def set_up(self):
        self.t_meco = self.mf * self.Ma_ce / self.T
        
def _calc_rho(t, y, params):
    H = y[0] * x_ref
    return atm.density(H) / rho_ref

def _calc_CD(t, y, params):
    if y[1] < 1.0:
        return params.CD
    else:
        return 2.0 * params.CD

def _calc_T_by_W(t, y, params):
    if t <= params.t_meco:
        return params.T / (1.0 - t * params.T / params.Ma_ce)
    else:
        return 0.0

def _calc_M(t, y, params):
    numerator = 1.0 - params.mf
    denumerator = 1.0 - t * params.T / params.Ma_ce
    
    return min(numerator/denumerator, 1.0)

def _func(t, y, params):
    T_by_W = _calc_T_by_W(t, y, params)
    rho = _calc_rho(t, y, params)
    CD = _calc_CD(t, y, params)
    M = _calc_M(t, y, params)
    
    Ma2 = y[1]**2 / params.Ma_L**2
    C = CD/params.CA_L
    
    ddot_x = T_by_W - rho * Ma2 * C * M - 1.0
    
    return (y[1], ddot_x)

def _turn_around(t, y, params):
    return y[1]

_turn_around.terminal = True
_turn_around.direction = -1

def solve_trajectory(t, y0, params):
    params.set_up()
    
    params.c0 = atm.speed_of_sound(0.0)
    params.rho_ref = atm.density(0.0)
    params.t_ref = c0/g
    params.ddot_x_ref = g
    params.dot_x_ref = ddot_x_ref*t_ref
    params.x_ref = dot_x_ref*t_ref
    
    return solve_ivp(_func, (t[0], t[-1]), y0, t_eval = t, args=(params, ), events=_turn_around)