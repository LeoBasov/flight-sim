import time
import os
import csv

class Writer:
	def __init__(self):
		self.file_dir = './output/' + time.strftime('%Y%m%d_%H%M%S', time.localtime())

	def write_to_file(self, kinetic_state, time):
		try:
			os.makedirs(self.file_dir)

		except FileExistsError:
			pass

		finally:
			self.write_kinetic_state(self.file_dir, kinetic_state, time)

	def write_kinetic_state(self, file_dir, kinetic_state, time):
		file_name = file_dir + '/kinetic_state.csv'
		row = [time, kinetic_state.position[0], kinetic_state.position[1], kinetic_state.velocity[0], kinetic_state.velocity[1]]

		with open(file_name, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(row)
