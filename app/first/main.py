#!/usr/bin/env python3

import sys

sys.path.append('../../.')

from flight_sim.simulation import Simulation

def main():
    sim = Simulation()

    sim.execute()

if __name__ == '__main__':
    main()
