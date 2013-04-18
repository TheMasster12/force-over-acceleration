#This class will be the backbone of the whole simulation.
import random.py

NUM_BODIES = 100;
DIM_X = 1000;
DIM_Y = 1000;
DIM_Z = 1000;
MASS_MIN = 0.000001 #1e-6 kg
MASS_MAX = 0.001 #1e-3 kg
VELOCITY_MIN = 0.01 #1e-2 m/s
VELOCITY_MAX = 100 #100 m/s

def run_simulation():
  #start graphics

  bodyArray = []
  for x in range(0,NUM_BODIES):
    ranX = random.random() * DIM_X
     ranY = random.random() * DIM_Y
     ranZ = random.random() * DIM_Z
     ranMass = random.uniform(MASS_MIN,MASS_MAX)
     ranVelocity = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
     bodyArray.append(Body(ranX,ranY,ranZ,ranMass,ranVelocity))

  for i in range(0, bodyArray.length):
    for j in range(i, bodyArray.length):
      bodyArray[i].interactWith(bodyArray[j])

  #paint
  return
