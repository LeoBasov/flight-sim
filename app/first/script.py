#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    g = 9.81
    ce = 2530 #[m/s]
    thrust_to_weight = 2.08
    empty_mass_frac = 0.3333
    PAX = 250

    fuel_fractions = np.linspace(0.4, 0.6, 100)
    m_tot = []

    for fraction in fuel_fractions:
        m_tot.append(PAX/(1.0 - empty_mass_frac - fraction))

    m_dot = np.array(m_tot)*thrust_to_weight*g/ce

    fig, axs = plt.subplots(nrows=1, ncols=2)

    axs[0].plot(fuel_fractions, m_tot)
    axs[0].set_xlabel('Fuel mass fraction [-]')
    axs[0].set_ylabel('Total mass [kg]')

    axs[1].plot(fuel_fractions, m_dot)
    axs[1].set_xlabel('Fuel mass fraction [-]')
    axs[1].set_ylabel('Mass flow [kg/s]')

    plt.show()

if __name__ == '__main__':
    main()
