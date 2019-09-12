from .flight_model import FlightModel

class Solver:
    def __init__(self, initial_fuel_mass, dt):
        self.dt = dt
        self.model = FlightModel(initial_fuel_mass)

        self.positions = []

    def execute(self):
        self.positions = []
        self.positions.append(self.model.position)

        while self.model.fuel_mass > 0.0:
            self.move_model()
            self.positions.append(self.model.position)
            self.model.process(self.dt)

    def move_model(self):
        totla_force = self.model.thrust() + self.model.drag() + self.model.weight_force() + self.model.lift()
        mass = self.model.total_mass()
        acceleration = totla_force/mass

        self.model.position += self.dt*self.model.velocity + 0.5*acceleration*self.dt*self.dt
        self.model.velocity += acceleration*self.dt
