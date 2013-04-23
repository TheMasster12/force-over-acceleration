#This class will be the backbone of the whole simulation.
import random,math

import body
import vector

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

NUM_BODIES = 100
DIM_X = 2000
DIM_Y = 2000
DIM_Z = 2000
MASS_MIN = 1e14
MASS_MAX = 1e16
VELOCITY_MIN = 1e-2 
VELOCITY_MAX = 100

CAM_DISTANCE = max([DIM_X,DIM_Y,DIM_Z]) * 1.5

bodyArray = []

def generateBodies():
  for x in xrange(NUM_BODIES):
    ranX = random.random() * DIM_X - (DIM_X / 2)
    ranY = random.random() * DIM_Y - (DIM_Y / 2)
    ranZ = random.random() * DIM_Z - (DIM_Z / 2)
    ranMass = random.uniform(MASS_MIN,MASS_MAX)
    
    '''
    ranVx = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVy = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVz = random.uniform(VELOCITY_MIN,VE100LOCITY_MAX)
    ranVelocity = vector.Vector(ranVx,ranVy,ranVz)
    '''

    ranVelocity = vector.zero()

    #bodyArray.append(body.Body(ranX,ranY,ranZ,ranMass,ranVelocity))
  v = 300
  m = 1e15
  d = 900
  bodyArray.append(body.Body(d, 0, 0, m, vector.Vector(0, v, 0)))
  bodyArray.append(body.Body(-d, 0, 0, m, vector.Vector(0, -v, 0)))
  bodyArray.append(body.Body(0, d, 0, m, vector.Vector(0, 0, v)))
  bodyArray.append(body.Body(0, -d, 0, m, vector.Vector(0, 0, -v)))
  bodyArray.append(body.Body(0, 0, d, m, vector.Vector(v, 0, 0)))
  bodyArray.append(body.Body(0, 0, -d, m, vector.Vector(-v, 0, 0)))
  
def simulateFrame():  
  forces = [x.totalForceOn(bodyArray) for x in bodyArray] # Force on each body
  for i in xrange(len(bodyArray)):
    bodyArray[i].move(forces[i])

def initFun():
  # Clear the canvas
  glClearColor(0.0,0.0,0.0,0.0)
  glColor3f(1.0,1.0,1.0)

  # Make things look nice
  glEnable(GL_POINT_SPRITE)
  glEnable(GL_POINT_SMOOTH)
  glEnable(GL_BLEND)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

  # First, load up the perspective.
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0, 1.0, 0.1, CAM_DISTANCE * 3)

  # Now, position the camera where it must be
  glMatrixMode(GL_MODELVIEW)
  gluLookAt(0.0, 0.0, CAM_DISTANCE, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def displayFun():
  simulateFrame()
  glClear(GL_COLOR_BUFFER_BIT)

  for b in bodyArray:
    glPushMatrix()
    glTranslate(b.x,b.y,b.z)
    glutSolidSphere(math.log(b.mass * 1e-14, 2) * 2, 20,20)
    glPopMatrix()

  glFlush()

def simulate_test():
  bodyArray = []
  bodyArray.append(body.Body(500,500,0,5.972e24,vector.Vector(0,0,0)))
  bodyArray.append(body.Body(499,500,6.371e6,1,vector.Vector(0,0,0)))
  bodyArray.append(body.Body(501,500,6.371e6,1,vector.Vector(0,0,0)))

  print(str(bodyArray[0]))
  print(str(bodyArray[1]))
  print(str(bodyArray[2]))

  for x in xrange(NUM_CYCLES):
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
  generateBodies()
  glutInit()
  glutInitWindowSize(1000,1000)
  glutCreateWindow("Force-Over-Acceleration")
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutDisplayFunc(displayFun)
  glutIdleFunc(displayFun) #Im pretty sure this is wrong
  initFun()
  glutMainLoop()
