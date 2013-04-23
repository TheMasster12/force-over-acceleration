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
VELOCITY_MIN = -1e4 
VELOCITY_MAX = 1e4

CAM_DISTANCE = max([DIM_X,DIM_Y,DIM_Z]) * 1.5
initialCameraDistance = CAM_DISTANCE

bodyArray = []
frameCount = 0
frameTimeHolder = int(round(time.time() * 1000))
avgFrameTime = 0
showData = True
startTime = time.time()
argHolder = [] 

def generateRandomBodies():
  for x in xrange(NUM_BODIES):
    addRandomBody()

def addRandomBody():
  global bodyArray
  ranX = random.random() * DIM_X - (DIM_X / 2)
  ranY = random.random() * DIM_Y - (DIM_Y / 2)
  ranZ = random.random() * DIM_Z - (DIM_Z / 2)
  ranMass = random.uniform(MASS_MIN,MASS_MAX)
  '''
  ranVx = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
  ranVy = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
  ranVz = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
  ranVelocity = vector.Vector(ranVx,ranVy,ranVz)
  '''
  ranVelocity = vector.zero()
  bodyArray.append(body.Body(ranX,ranY,ranZ,ranMass,ranVelocity))

def removeBody():
  global bodyArray
  del bodyArray[random.randint(0,len(bodyArray) - 1)]

def readBodies(args):
  global bodyArray
  for arg in args:
    b = [float(x) for x in arg.split()] # List of numbers that identify body
    v = vector.Vector(b[4], b[5], b[6])
    bodyArray.append(body.Body(b[0], b[1], b[2], b[3], v))

def simulateFrame(): 
  forces = [x.totalForceOn(bodyArray) for x in bodyArray]
  for i in xrange(len(bodyArray)):
    bodyArray[i].move(forces[i],avgFrameTime)

def initFun():
  # Clear the canvas
  glClearColor(0.0,0.0,0.0,0.0)

  # Make things look nice
  glEnable(GL_POINT_SPRITE)
  glEnable(GL_POINT_SMOOTH)
  glEnable(GL_BLEND)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

  # First, load up the perspective.
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0, 1.0, 0.1, CAM_DISTANCE * 30)
 
  orientCamera()

def orientCamera():
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluLookAt(0.0, 0.0, CAM_DISTANCE, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def begin2D(withDepthTest):
  glMatrixMode(GL_PROJECTION)
  glPushMatrix()
  glLoadIdentity()
  glOrtho(0, 1000, 0, 1000, 0, 1)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

def end2D():
  glMatrixMode(GL_PROJECTION)
  glPopMatrix()
  orientCamera()

def display():
  global frameCount,frameTimeHolder,avgFrameTime
  simulateFrame()
  glClear(GL_COLOR_BUFFER_BIT)

  # Render bodies
  glMatrixMode(GL_MODELVIEW)
  glColor3f(1.0, 1.0, 1.0)
  for b in bodyArray:
    glPushMatrix()
    glTranslate(b.x,b.y,b.z)
    glutSolidSphere(math.log(b.mass * 1e-14, 2) * 2, 20,20)
    glPopMatrix()

  # Show render data on screen
  if showData:
    if avgFrameTime == 0:
      fpsStr = "Framerate: N/A"
      avgStr = "Average  : N/A"
    else:
      fpsStr = "Framerate: " + str(1.0/avgFrameTime) + " fps"
      avgStr = "Average  : " + str(avgFrameTime) + " s"
    bodStr = "Bodies   : " + str(len(bodyArray))
    timStr = "Time     : " + str(int(round(time.time() - startTime))) + " s"

    begin2D(False)
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2f(20,80)
    glutBitmapString(GLUT_BITMAP_9_BY_15, fpsStr)
    glRasterPos2f(20,60)
    glutBitmapString(GLUT_BITMAP_9_BY_15, avgStr)
    glRasterPos2f(20,40)
    glutBitmapString(GLUT_BITMAP_9_BY_15, bodStr)
    glRasterPos2f(20,20)
    glutBitmapString(GLUT_BITMAP_9_BY_15, timStr)
    end2D()

  glFlush() # Finish all drawing before this line

  # Update render data
  frameCount += 1
  if frameCount % 10 == 0:
    lastTenFramesTime = int(round(time.time() * 1000.0)) - frameTimeHolder
    avgFrameTime = lastTenFramesTime / 10000.0
    frameTimeHolder = int(round(time.time() * 1000.0)) 

def refreshBodyArray():
  global bodyArray
  bodyArray = []

  if len(sys.argv) < 2:
    generateRandomBodies()
  else:
    readBodies(argHolder)

def handleKeypress(key,x,y):
  global showData, startTime, frameCount, avgFrameTime, frameTimeHolder
  global CAM_DISTANCE

  if key == 'q':
    sys.exit(0)

  if key == 'r':
    frameCount = 0
    avgFrameTime = 0
    frameTimeHolder = int(round(time.time() * 1000.0))
    startTime = time.time()

    # Uncomment to play with zooming
    #CAM_DISTANCE = initialCameraDistance
    #orientCamera()

    refreshBodyArray()

  if key == 'f':
    showData = not showData

  if key == 'n':
    addRandomBody()

  if key == 'd':
    removeBody()

def handleMouse(button, state, x, y):
  global CAM_DISTANCE

  # Uncomment lines below to play with zooming
  if button == 3:
    if state == GLUT_DOWN:
      if CAM_DISTANCE > 200: CAM_DISTANCE -= 200
      orientCamera()
  if button == 4:
    if state == GLUT_DOWN:
      CAM_DISTANCE += 200
      orientCamera()

if __name__ == '__main__':
  #Initialize GLUT
  glutInit()
  glutInitWindowSize(1000,1000)
  glutCreateWindow("Force-Over-Acceleration")
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutKeyboardFunc(handleKeypress)
  glutMouseFunc(handleMouse)
  glutDisplayFunc(display)
  glutIdleFunc(display)

  #Initialize everything else
  if len(sys.argv) >= 2:
    argHolder = sys.stdin.readlines()
  refreshBodyArray()
  initFun()
  glutMainLoop()
