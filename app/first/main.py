#!/usr/bin/env python3

import sys
import math
import numpy as np

sys.path.append('../../.')

from flight_sim.simulation import Simulation
from flight_sim.simulation import NumericParameters
from flight_sim.simulation import AbortCriterium
from flight_sim.models.plane import Plane
from flight_sim.models.engine import JP5_H2O2
from flight_sim.models.engine import HTPB_N2O
from flight_sim.visualizer import Visualizer
from flight_sim.models.aero import Simple

def main():
	visualizer = Visualizer()

	cargo_mass = 300
	fuel_mass_fractions = [0.65]
	empty_mass_frac = 0.32
	mass_flow = 80
	file_names_dt_itter = []

	for fuel_mass_fraction in fuel_mass_fractions:
		parameters = {}

		parameters["numeric_parameters"] = NumericParameters()
		parameters["abort_criterium"] = AbortCriterium()
		parameters["plane"] = set_up_HTPB_N2O_plane(mass_flow, cargo_mass, empty_mass_frac, fuel_mass_fraction)

		parameters['test_case_name'] = "FIRST TEST"
		parameters['test_case_specifics'] = ["Simple JP5 H2O2 plane"]

		sim = Simulation()

		sim.set_up(**parameters)
		sim.execute()

		file_names_dt_itter.append([sim.writer.kinetic_state_file_name, sim.numeric_parameters.dt, sim.numeric_parameters.itteration])

	visualizer.plot_heights(file_names_dt_itter, fuel_mass_fractions)

def set_up_HTPB_N2O_plane(mass_flow, cargo_mass, empty_mass_frac, fuel_mass_fraction):
	total_mass = cargo_mass/(1.0 - empty_mass_frac - fuel_mass_fraction)
	plane = Plane()
	ref_radius = 2.2
	ref_length = 18
	ref_drag_area = 5.8
	ref_lift_area = 19.8
	wetted_area = 47

	plane.fuel_mass = total_mass*fuel_mass_fraction
	plane.dry_mass  = total_mass*empty_mass_frac

	plane.aero_model = Simple(ref_radius = ref_radius, ref_length = ref_length, ref_drag_area = ref_drag_area, ref_lift_area = ref_lift_area, wetted_area = wetted_area)
	plane.engine_model = HTPB_N2O(mass_flow)

	plane.kinetic_state.angle = 0.5*math.pi

	return plane

if __name__ == '__main__':
	main()
