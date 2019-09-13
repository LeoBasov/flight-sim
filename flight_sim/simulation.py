"""
Main module.

"""

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

	def set_up(self, **kwargs):
		self.numeric_parameters = kwargs['numeric_parameters']
		self.abort_criterium = kwargs['abort_criterium']
		self.plane = kwargs['plane']

		self.test_case_name = kwargs['test_case_name']
		self.test_case_specifics = kwargs['test_case_specifics']

	def execute(self):
		self.print_header()

		while self.abort_criterium.passed(self.plane):
			self.flight_solver.execute(self.plane)
			self.aero_solver.execute(self.plane)
			self.kinetic_solver.execute(self.plane)

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

class AbortCriterium:
	def __init__(self):
		pass

	def passed(self, place):
		return False
