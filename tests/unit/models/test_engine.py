import unittest
import sys

sys.path.append('../../.')

import flight_sim.models.engine as eng

class JP5_H2O2_Test(unittest.TestCase):
	def test_get_ce(self):
		mass_flow = 10
		height1 = 0
		height2 = 100000
		engine = eng.JP5_H2O2(mass_flow)

		ce_ground = engine.get_ce((0, height1))
		ce_vacuum = engine.get_ce((0, height2))

		self.assertAlmostEqual(ce_ground, engine.ce_ground, 3)
		self.assertAlmostEqual(ce_vacuum, engine.ce_vacuum, 3)

	def test_thrust(self):
		mass_flow = 10
		height1 = 0
		height2 = 100000
		engine = eng.JP5_H2O2(mass_flow)

		ce_ground = engine.get_ce((0, height1))
		ce_vacuum = engine.get_ce((0, height2))

		thrust_ground = engine.thrust((0, height1), (0, 0))
		thrust_vacuum = engine.thrust((0, height2), (0, 0))

		self.assertAlmostEqual(ce_ground*mass_flow, thrust_ground, 3)
		self.assertAlmostEqual(ce_vacuum*mass_flow, thrust_vacuum, 3)
