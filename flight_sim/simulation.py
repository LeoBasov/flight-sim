"""
Main module.

"""

import numpy as np
from . import solver

class Simulation:
	def __init__(self):
		self.numeric_parameters = None
		self.abort_criterium = None
		self.plane = None

		self.flight_solver = solver.Flight()
		self.aero_solver = solver.Aero()
		self.kinetic_solver = solver.Kinetic()

		self.test_case_name = "PLACE HOLDER"
		self.test_case_specifics = ["PLACE HOLDER"]

		self.flight_path = []

	def set_up(self, **kwargs):
		self.numeric_parameters = kwargs['numeric_parameters']
		self.abort_criterium = kwargs['abort_criterium']
		self.plane = kwargs['plane']

		self.test_case_name = kwargs['test_case_name']
		self.test_case_specifics = kwargs['test_case_specifics']

	def execute(self):
		self.print_header()

		self.flight_path.append(np.array(self.plane.kinetic_state.position))

		while self.abort_criterium.passed(self.plane, self.numeric_parameters):
			print("ITTERATION: {:9d} Height: {:9.3f}".format(self.numeric_parameters.itteration, self.plane.kinetic_state.position[1]), end="\r", flush=True)

			self.flight_solver.execute(self.plane, self.numeric_parameters.dt)
			self.aero_solver.execute(self.plane, self.numeric_parameters.dt)
			self.kinetic_solver.execute(self.plane, self.numeric_parameters.dt)
			self.flight_path.append(np.array(self.plane.kinetic_state.position))
			self.numeric_parameters.advace()

		print("")
		print("Done")

		self.print_footer()

	def print_header(self):
		print(80*"=")
		print("FLIGHT PATH ANALYSIS TOOL")
		print("(c) 2019, Leo Basov")
		print(80*"-")
		print(self.test_case_name)

		for specific in self.test_case_specifics:
			print(specific)

		print(80*"-")

	def print_footer(self):
		print(80*"-")
		print("Execution finished")
		print(80*"=")

class NumericParameters:
	def __init__(self, dt = 1.0e-3):
		self.dt = dt
		self.itteration = 0

	def advace(self):
		self.itteration += 1

	def time(self):
		return self.itteration*self.dt

class AbortCriterium:
	def __init__(self):
		self.max_itteration = 1000

	def passed(self, plane, numeric_parameters):
		if numeric_parameters.itteration > self.max_itteration:
			return False
		else:
			if plane.kinetic_state.position[1] < 0.0:
				return False
			else:
				return True
