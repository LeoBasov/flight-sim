import time
import os
import csv

class Writer:
	def __init__(self):
		self.file_dir = './output/' + time.strftime('%Y%m%d_%H%M%S', time.localtime())

		self.kinetic_state_file_name = self.file_dir + '/kinetic_state.csv'

	def write_to_file(self, kinetic_state, time):
		try:
			os.makedirs(self.file_dir)

			self.write_kinetic_state_header()

		except FileExistsError:
			pass

		finally:
			self.write_kinetic_state(kinetic_state, time)

	def write_kinetic_state_header(self):
		row = ['#t', '#pos_x', '#pos_y', '#vel_x', '#vel_y']

		with open(self.kinetic_state_file_name, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(row)

	def write_kinetic_state(self, kinetic_state, time):
		row = [time, kinetic_state.position[0], kinetic_state.position[1], kinetic_state.velocity[0], kinetic_state.velocity[1]]

		with open(self.kinetic_state_file_name, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(row)
