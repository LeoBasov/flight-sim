import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self):
        pass

    def plot_height(self, flight_path, dt, itterations):
        time = np.linspace(0, dt*itterations, itterations + 1)
        height = []

        for position in flight_path:
            height.append(position[1])

        plt.plot(time, height)
        plt.show()
