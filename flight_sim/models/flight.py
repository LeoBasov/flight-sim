"""
Describes the reaction of a virtual pilot to the current state

"""

class Pilot:
    def __init__(self):
        pass

    def fly(self, plane, dt):
        plane.fire_engine(dt)
