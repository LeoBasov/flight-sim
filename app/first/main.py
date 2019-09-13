#!/usr/bin/env python3

import sys

sys.path.append('../../.')

from flight_sim.simulation import Simulation
from flight_sim.simulation import NumericParameters
from flight_sim.simulation import AbortCriterium
from flight_sim.models import plane

def main():
	parameters = {}

	parameters["numeric_parameters"] = NumericParameters()
	parameters["abort_criterium"] = AbortCriterium()
	parameters["plane"] = plane.Plane()

	parameters['test_case_name'] = "FIRST TEST"
	parameters['test_case_specifics'] = ["Simple JP5 H2O2 plane"]

	sim = Simulation()

	sim.set_up(**parameters)
	sim.execute()

if __name__ == '__main__':
	main()
