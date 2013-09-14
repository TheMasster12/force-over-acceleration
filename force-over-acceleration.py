import sys
import simulator

if __name__ == '__main__':
    sim = simulator.Simulator()

    if len(sys.argv) >= 2:
        sim.argHolder = sys.stdin.readlines()

#    sim.refreshBodyArray()
#    sim.renderEngine.start()
    sim.restartSimulation()
    sim.renderEngine.start()

