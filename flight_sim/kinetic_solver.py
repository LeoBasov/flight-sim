from .flight_model import FlightModel

class Solver:
    def __init__(self, initial_fuel_mass, dt):
        self.time = 0
        self.dt = dt
        self.model = FlightModel(initial_fuel_mass)

        self.positions_x = []
        self.positions_y = []
        self.times = []

    def execute(self):
        self.positions_x.append(self.model.position[0])
        self.positions_y.append(self.model.position[1])
        self.times.append(self.time)

        while True:
            self.move_model()

            if  self.model.position[1] < self.positions_y[-1]:
                break

            self.positions_x.append(self.model.position[0])
            self.positions_y.append(self.model.position[1])
            self.model.process(self.dt)

            self.time += self.dt
            self.times.append(self.time)

    def move_model(self):
        totla_force = self.model.thrust() + self.model.drag() + self.model.weight_force() + self.model.lift()
        mass = self.model.total_mass()
        acceleration = totla_force/mass

        self.model.position += self.dt*self.model.velocity + 0.5*acceleration*self.dt*self.dt
        self.model.velocity += acceleration*self.dt
