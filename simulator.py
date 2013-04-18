#This class will be the backbone of the whole simulation.
import random
import body
import vector

NUM_BODIES = 10 
DIM_X = 1000
DIM_Y = 1000
DIM_Z = 1000
MASS_MIN = 1e-6
MASS_MAX = 1e-3
VELOCITY_MIN = 1e-2 
VELOCITY_MAX = 100
NUM_CYCLES = 10000

def simulate():
  bodyArray = []

  for x in xrange(0,NUM_BODIES):
    ranX = random.random() * DIM_X
    ranY = random.random() * DIM_Y
    ranZ = random.random() * DIM_Z
    ranMass = random.uniform(MASS_MIN,MASS_MAX)

    ranVx = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVy = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVz = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVelocity = vector.Vector(ranVx,ranVy,ranVz)

    bodyArray.append(body.Body(ranX,ranY,ranZ,ranMass,ranVelocity))
  
  print("Pre-Simulation:")
  for x in xrange(0,NUM_BODIES):
    print(str(bodyArray[x]))

    for i in xrange(0, len(bodyArray)):
      for j in xrange(i+1,len(bodyArray)):
        bodyArray[i].interactWith(bodyArray[j])
  
  print("\nPost-Simulation:")
  for x in xrange(0,NUM_BODIES):
    print(str(bodyArray[x]))

  return

def simulate_test():
  bodyArray = []
  bodyArray.append(body.Body(500,500,0,5.972e24,vector.Vector(0,0,0)))
  bodyArray.append(body.Body(499,500,6.371e6,1,vector.Vector(0,0,0)))
  bodyArray.append(body.Body(501,500,6.371e6,1,vector.Vector(0,0,0)))

  print(str(bodyArray[0]))
  print(str(bodyArray[1]))
  print(str(bodyArray[2]))

  for x in xrange(0,NUM_CYCLES):
    bodyArray[0].interactWith(bodyArray[1])
    bodyArray[1].interactWith(bodyArray[0])
    bodyArray[0].interactWith(bodyArray[2])
    bodyArray[2].interactWith(bodyArray[0])
    bodyArray[1].interactWith(bodyArray[2])
    bodyArray[2].interactWith(bodyArray[1])

  print(str(bodyArray[0]))
  print(str(bodyArray[1]))
  print(str(bodyArray[2]))

  return

if __name__ == '__main__':
  #simulate_test()
  simulate()
