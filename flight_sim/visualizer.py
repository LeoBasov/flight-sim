import matplotlib.pyplot as plt
import numpy as np
import csv

class Visualizer:
	def __init__(self):
		pass

	def plot_height(self, kinetic_state_file_name, dt, itterations):
		karman_line = 100000 #[m]
		time = np.linspace(0, dt*itterations, itterations + 1)
		height = []
		space = karman_line*np.ones(itterations + 1)
		skip = True

		with open(kinetic_state_file_name) as file:
			reader = csv.reader(file, delimiter=',')

			for row in reader:
				if skip:
					skip = False
				else:
					height.append(float(row[2]))

		time = np.linspace(0, dt*itterations, len(height))
		space = karman_line*np.ones(len(height))

		plt.plot(time, height, label = 'Flight height')
		plt.plot(time, space, label = 'Karman Line', linestyle =  '--')
		plt.legend()
		plt.xlabel('Flight time [s]')
		plt.ylabel('Altitude [m]')
		plt.show()

	def plot_heights(self, file_names_dt_itter, fuel_mass_fractions):
		times_heights = []
		karman_line = 100000 #[m]
		max_len = 0

		for tuple in file_names_dt_itter:
			height = []

			with open(tuple[0]) as file:
				reader = csv.reader(file, delimiter=',')
				skip = True

				for row in reader:
					if skip:
						skip = False
					else:
						height.append(float(row[2]))

			time = np.linspace(0, tuple[1]*tuple[2], len(height))

			times_heights.append([time, height])

		for i in range(len(times_heights)):
			plt.plot(times_heights[i][0], times_heights[i][1], label = 'Fuel mass fraction: ' + str(fuel_mass_fractions[i]))

			if max_len > len(times_heights[i][0]):
				max_len = len(times_heights[i][0])

		space = karman_line*np.ones(len(height))

		plt.plot(time, space, label = 'Karman Line', linestyle =  '--')

		plt.legend()
		plt.xlabel('Flight time [s]')
		plt.ylabel('Altitude [m]')
		plt.show()
