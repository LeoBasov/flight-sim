#!/usr/bin/env python3

import sys
import math

sys.path.append('../../.')

from flight_sim.simulation import Simulation
from flight_sim.simulation import NumericParameters
from flight_sim.simulation import AbortCriterium
from flight_sim.models.plane import Plane
from flight_sim.models.engine import JP5_H2O2
from flight_sim.visualizer import Visualizer
from flight_sim.models.aero import Simple

def main():
	parameters = {}

	parameters["numeric_parameters"] = NumericParameters()
	parameters["abort_criterium"] = AbortCriterium()
	parameters["plane"] = set_up_plane()

	parameters['test_case_name'] = "FIRST TEST"
	parameters['test_case_specifics'] = ["Simple JP5 H2O2 plane"]

	sim = Simulation()
	visualizer = Visualizer()

	sim.set_up(**parameters)
	sim.execute()

	visualizer.plot_height(sim.writer.kinetic_state_file_name, sim.numeric_parameters.dt, sim.numeric_parameters.itteration)

def set_up_plane():
	mass_flow = 30
	plane = Plane()

	plane.fuel_mass = 3500
	plane.dry_mass = (1/2)*plane.fuel_mass

	plane.aero_model = Simple()
	plane.engine_model = JP5_H2O2(mass_flow)

	plane.kinetic_state.angle = 0.5*math.pi

	return plane

if __name__ == '__main__':
	main()
