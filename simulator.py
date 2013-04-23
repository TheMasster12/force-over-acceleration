#This class will be the backbone of the whole simulation.
import random,math,time
import body,vector

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
frameCount = 0
frameTimeHolder= int(round(time.time() * 1000))

def generateRandomBodies():
  global bodyArray
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

    bodyArray.append(body.Body(ranX,ranY,ranZ,ranMass,ranVelocity))

def readBodies(args):
  global bodyArray
  for arg in args:
    b = [float(x) for x in arg.split()]
    v = vector.Vector(b[4], b[5], b[6])
    bodyArray.append(body.Body(b[0], b[1], b[2], b[3], v))

def simulateFrame(): 
  global bodyArray
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
  global bodyArray,frameCount,frameTimeHolder
  simulateFrame()
  glClear(GL_COLOR_BUFFER_BIT)

  for b in bodyArray:
    glPushMatrix()
    glTranslate(b.x,b.y,b.z)
    glutSolidSphere(math.log(b.mass * 1e-14, 2) * 2, 20,20)
    glPopMatrix()

  glFlush()

  frameCount += 1
  if frameCount % 10 == 0:
    print(1.0 / ((int(round(time.time() * 1000)) - frameTimeHolder) / 10000.0))
    frameTimeHolder = int(round(time.time() * 1000)) 

def handleKeypress(key,x,y):
  if key == 'q':
    sys.exit(0)
  if key == 'r':
    print("restart")

if __name__ == '__main__':
  glutInit()
  glutInitWindowSize(1000,1000)
  glutCreateWindow("Force-Over-Acceleration")
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutKeyboardFunc(handleKeypress)
  glutDisplayFunc(displayFun)
  glutIdleFunc(displayFun) #Im pretty sure this is wrong

  if len(sys.argv) < 2:
    generateRandomBodies()
  else:
    readBodies(sys.stdin.readlines())

  initFun()
  glutMainLoop()
