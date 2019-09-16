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
