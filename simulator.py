#This class will be the backbone of the whole simulation.
import random
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
bodyArray = []

def generateBodies():
  for x in xrange(NUM_BODIES):
    ranX = random.random() * DIM_X
    ranY = random.random() * DIM_Y
    ranZ = random.random() * DIM_Z
    ranMass = random.uniform(MASS_MIN,MASS_MAX)
    
    '''
    ranVx = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVy = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVz = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVelocity = vector.Vector(ranVx,ranVy,ranVz)
    '''

    ranVelocity = vector.zero()

    bodyArray.append(body.Body(ranX,ranY,ranZ,ranMass,ranVelocity))
  
def simulateFrame():  
  forces = [x.totalForceOn(bodyArray) for x in bodyArray]
  for i in xrange(len(bodyArray)):
    bodyArray[i].move(forces[i])

def initFun():
  glClearColor(1.0,1.0,1.0,0.0)
  glColor3f(0.0,0.0,0.0)
  glEnable(GL_POINT_SPRITE)
  glEnable(GL_POINT_SMOOTH)
  glEnable(GL_BLEND)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0.0,1000.0,0.0,1000.0)

def displayFun():
  simulateFrame()

  glClear(GL_COLOR_BUFFER_BIT)

  for b in bodyArray:
    glPointSize(b.mass * 1e-15)
    glBegin(GL_POINTS)
    glVertex2f(b.x,b.y)
    glEnd()

  glFlush()

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
  generateBodies()
  glutInit()
  glutInitWindowSize(1000,1000)
  glutCreateWindow("Force-Over-Acceleration")
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutDisplayFunc(displayFun)
  glutIdleFunc(displayFun) #Im pretty sure this is wrong
  initFun()
  glutMainLoop()
