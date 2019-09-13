#!/usr/bin/env python3

import sys

sys.path.append('../../.')

from flight_sim.simulation import Simulation
from flight_sim.simulation import NumericParameters
from flight_sim.simulation import AbortCriterium
from flight_sim.models.plane import Plane

def main():
	parameters = {}

	parameters["numeric_parameters"] = NumericParameters()
	parameters["abort_criterium"] = AbortCriterium()
	parameters["plane"] = set_up_plane()

	parameters['test_case_name'] = "FIRST TEST"
	parameters['test_case_specifics'] = ["Simple JP5 H2O2 plane"]

	sim = Simulation()

	sim.set_up(**parameters)
	sim.execute()

def set_up_plane():
	plane = Plane()

	plane.dry_mass = 1000
	plane.fuel_mass = 2000

	return plane

if __name__ == '__main__':
	main()
