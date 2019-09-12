#!/usr/bin/env python3

import sys

sys.path.append('../.')

from flight_sim.atmosphere import Atmosphere
from flight_sim.flight_model import FlightModel
from flight_sim.kinetic_solver import Solver

def atmospehere_test():
    import numpy as np
    import matplotlib.pyplot as plt

    height = np.linspace(0, 100000, 10000)
    pressure = []
    rho = []
    temperature = []
    speed_of_sound = []
    atm = Atmosphere()

    for h in height:
        pressure.append(atm.pressure(h))
        rho.append(atm.density(h))
        temperature.append(atm.temperature(h))
        speed_of_sound.append(atm.speed_of_sound(h))

    fig, ax = plt.subplots(2, 2)

    ax[0, 0].plot(height, pressure, label = 'Pressure')
    ax[0, 1].plot(height, rho, label = 'rho')
    ax[1, 0].plot(height, temperature, label = 'temperature')
    ax[1, 1].plot(height, speed_of_sound, label = 'speed_of_sound')

    ax[0, 0].legend()
    ax[0, 1].legend()
    ax[1, 0].legend()
    ax[1, 1].legend()

    plt.show()

def flight_model_test():
    fuel_mass = 1500
    plane = FlightModel(fuel_mass)

    print("Fuel mass:", plane.fuel_mass)
    print("Dry mass:", plane.dry_mass)
    print("Total mass:", plane.total_mass())

def solver_test():
    initial_fuel_mass = 1500
    dt = 1e-3
    solver = Solver(initial_fuel_mass, dt)

    solver.execute()

def main():
    #atmospehere_test()
    #flight_model_test()
    solver_test()

if __name__ == '__main__':
    main()
