"""
dimensionless kinetics for rocket propelled ascend using constant thrust
"""

import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def calc_rho(x, xref):
    n = 1.235
    T_0 = 288.15
    T_i = 216.65
    R = 287.05
    x_i = 11000/xref
    
    if x < 11000/xref:
        return math.pow(1.0 - ((n - 1.0)/n)*(g/(R*T_0))*x*xref, (1.0/(n - 1.0)))
    else:
        return (0.3639 / 1.225) * math.exp(-g*(x - x_i)*xref/(R*T_i))

def calc_ddotx(t, T, C_D, C_L_TO, c_TO, mu, rho, dotx, x):
    tau = (1 - t[-1]*T)
    
    return T/tau - (C_D/C_L_TO) * (c_TO**2 * rho * dotx[-1]**2)/tau - mu

def calc_ddotx_no_T(t, m_f, C_D, C_L_TO, c_TO, mu, rho, dotx, x):
    tau = (1 - m_f)
    
    return  - (C_D/C_L_TO) * (c_TO**2 * rho * dotx[-1]**2)/tau - mu

def calc_dotx(dt, ddotx, dotx):
    return dotx[-1] + dt * ddotx[-1]

def calc_x(dt, ddotx, dotx, x):
    return x[-1] + dt * dotx[-1] + 0.5 * ddotx[-1] * dt**2

def calc_T(H):
    H_i = 11000
    n = 1.235
    T_0 = 288.15
    T_i = 216.65
    R = 287.05
    
    if H < H_i:
        return T_0* (1.0 - ((n - 1.0)/n)*(g/(R*T_0))*(H))
    else:
        return T_i
    
def calc_a(H):
    K = 1.405
    R = 287.05
    return math.sqrt(K*R*calc_T(H))

if __name__ == '__main__':
    c_e = 2500
    xref = c_e**2 / g
    v_TO = 43
    
    # values open to optimization
    #----------------------------
    T = 2
    m_f = 0.6
    C_D = 0.005 # here I need a model as C_D = fn(dotx)
    C_L_TO = 0.7
    #----------------------------
    
    c_TO = c_e / v_TO
    mu = 1
    
    dt = 0.001
    
    t = [0]
    dotx = [0]
    x = [0]
    ddotx = [calc_ddotx(t, T, C_D, C_L_TO, c_TO, mu, 1, dotx, x)]
    
    while t[-1] < (m_f / T):
        t.append(t[-1] + dt)
        x.append(calc_x(dt, ddotx, dotx, x))
        dotx.append(calc_dotx(dt, ddotx, dotx))
        ddotx.append(calc_ddotx(t, T, C_D, C_L_TO, c_TO, mu, calc_rho(x[-1], xref), dotx, x))
        
    while dotx[-1] > 0.0:
        t.append(t[-1] + dt)
        x.append(calc_x(dt, ddotx, dotx, x))
        dotx.append(calc_dotx(dt, ddotx, dotx))
        ddotx.append(calc_ddotx_no_T(t, m_f, C_D, C_L_TO, c_TO, mu, calc_rho(x[-1], xref), dotx, x))
        
    a = [calc_a(xi*xref) for xi in x]
        
    x = np.array(x)*(xref/1e5)
    dotx = [dotx[i]*c_e/a[i] for i in range(len(dotx))]
    t = np.array(t)*(T/m_f)
        
    plt.plot(t, x)
    plt.xlabel("$t \;/\; t_{burn}$")
    plt.ylabel("$x \;/\; H_K$")
    
    plt.show()
    
    plt.plot(t, dotx)
    plt.xlabel("$t \;/\; t_{burn}$")
    plt.ylabel("$Ma$")
    
    plt.show()
    

    plt.plot(t, ddotx, '.', markersize=1)
    plt.xlabel("$t \;/\; t_{burn}$")
    plt.ylabel("$\ddot{x} \;/\; g$")
    
    plt.show()