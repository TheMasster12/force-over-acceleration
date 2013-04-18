#This class will be the backbone of the whole simulation.
import random
import body
import vector

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

NUM_BODIES = 10 
DIM_X = 1000
DIM_Y = 1000
DIM_Z = 1000
MASS_MIN = 1e-6
MASS_MAX = 1e-3
VELOCITY_MIN = 1e-2 
VELOCITY_MAX = 100
bodyArray = []

def generateBodies():
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
  
def simulateFrame():  
  for i in xrange(0, len(bodyArray)):
    for j in xrange(i+1,len(bodyArray)):
      bodyArray[i].interactWith(bodyArray[j])

def initFun():
  glClearColor(1.0,1.0,1.0,0.0)
  glColor3f(0.0,0.0,0.0)
  glPointSize(10.0)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0.0,1000.0,0.0,1000.0)

def displayFun():
  print("here")
  simulateFrame()

  glClear(GL_COLOR_BUFFER_BIT)
  glBegin(GL_POINTS)

  for i in xrange(0,NUM_BODIES):
    glVertex2f(bodyArray[i].x,bodyArray[i].y)
    glVertex2f(bodyArray[i].x + 10.0,bodyArray[i].y + 10.0)

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
  glutInit()
  glutInitWindowSize(1000,1000)
  glutCreateWindow("Force-Over-Acceleration")
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutDisplayFunc(displayFun)
  initFun()
  generateBodies()
  glutMainLoop()
