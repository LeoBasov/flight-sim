#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    g = 9.81
    ce = 2530 #[m/s]
    thrust_to_weight = 2.08
    empty_mass_frac = 0.3333
    PAX = 250

    fuel_fractions = np.linspace(0.4, 0.98*(1.0 - empty_mass_frac), 100)
    m_tot = []

    for fraction in fuel_fractions:
        m_tot.append(PAX/(1.0 - empty_mass_frac - fraction))

    m_dot = np.array(m_tot)*thrust_to_weight*g/ce
    m_fuel = []
    burn_time = []

    for i in range(len(m_tot)):
        m_fuel.append(m_tot[i]*fuel_fractions[i])
        burn_time.append(m_tot[i]*fuel_fractions[i]/m_dot[i])

    fig, axs = plt.subplots(nrows=2, ncols=2)

    axs[0][0].plot(fuel_fractions, m_tot)
    axs[0][0].set_xlabel('Fuel mass fraction [-]')
    axs[0][0].set_ylabel('Total mass [kg]')

    axs[0][1].plot(fuel_fractions, m_dot)
    axs[0][1].set_xlabel('Fuel mass fraction [-]')
    axs[0][1].set_ylabel('Mass flow [kg/s]')

    axs[1][0].plot(fuel_fractions, m_fuel)
    axs[1][0].set_xlabel('Fuel mass fraction [-]')
    axs[1][0].set_ylabel('Fuel mass [kg]')

    axs[1][1].plot(fuel_fractions, burn_time)
    axs[1][1].set_xlabel('Fuel mass fraction [-]')
    axs[1][1].set_ylabel('Burn time [s]')

    fig.suptitle('PAX = {} kg, c_e = {} m/s, T/W = {}, empty mass fraction = {}'.format(PAX, ce, thrust_to_weight, empty_mass_frac))

    plt.show()

    print(fuel_fractions[-1])

if __name__ == '__main__':
    main()
