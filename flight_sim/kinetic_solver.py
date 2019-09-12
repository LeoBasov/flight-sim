from .flight_model import FlightModel

class Solver:
    def __init__(self, initial_fuel_mass):
        self.model = FlightModel(initial_fuel_mass)
