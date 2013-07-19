import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Display(object):

  def __init__(self,sim):
    self.simulator = sim
    self.frameCount = 0
    self.frameTimeHolder = int(round(time.time() * 1000))
    self.avgFrameTime = 0
    self.startTime = time.time()

    self.showData = True
    self.isPaused = False
    self.rho = 0
    self.theta = 0
    self.phi = 0

    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("Force-Over-Acceleration")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutKeyboardFunc(self.simulator.handleKeypress)
    glutSpecialFunc(self.simulator.handleSpecial)
    glutMouseFunc(self.simulator.handleMouse)
    glutDisplayFunc(self.display)
    glutIdleFunc(self.display)

  def start(self):
    """Initializes all OpenGL things."""
    glClearColor(0.0,0.0,0.0,0.0)

    # Make things look nice
    glEnable(GL_POINT_SPRITE)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # First, load up the perspective.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, rho * 30)
   
    self.orientCamera()
    glutMainLoop()
    
  def orientCamera(self):
    """Moves and turns the camera based on spherical coordinates."""
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    x = self.rho * math.sin(self.phi) * math.sin(self.theta)
    y = self.rho * math.cos(self.phi) 
    z = self.rho * math.sin(self.phi) * math.cos(self.theta)
    gluLookAt(x, y, z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

  def displayBodies(self):
    """Render the bodies."""
    glMatrixMode(GL_MODELVIEW)
    glColor3f(1.0, 1.0, 1.0)
    for b in self.simulator.bodyArray:
      glPushMatrix()
      glTranslate(b[0],b[1],b[2])
      glutSolidSphere(math.log(b[3] * 1e-14, 2) * 2, 20,20)
      glPopMatrix()

  def displayData(self):
    """Render data, if showData is set to True."""
    if self.showData:
      if self.avgFrameTime == 0:
        fpsStr = "Framerate: N/A"
        avgStr = "Average  : N/A"
      else:
        fpsStr = "Framerate: " + str(1.0/self.avgFrameTime) + " fps"
        avgStr = "Average  : " + str(self.avgFrameTime) + " s"
      bodStr = "Bodies   : " + str(self.simulator.bodyArray.shape[0])
      timStr = "Time     : " + str(int(round(time.time() - self.startTime))) + " s"
      if self.simulator.bodyArray.shape[0] < 1:
        cenStr = "Center   : N/A"
      else:
        cenStr = "Center   : " + str(self.simulator.barycenter())

      begin2D()
      glColor3f(1.0, 0.0, 0.0)
      glRasterPos2f(20,100)
      glutBitmapString(GLUT_BITMAP_9_BY_15, cenStr)
      glRasterPos2f(20,80)
      glutBitmapString(GLUT_BITMAP_9_BY_15, fpsStr)
      glRasterPos2f(20,60)
      glutBitmapString(GLUT_BITMAP_9_BY_15, avgStr)
      glRasterPos2f(20,40)
      glutBitmapString(GLUT_BITMAP_9_BY_15, bodStr)
      glRasterPos2f(20,20)
      glutBitmapString(GLUT_BITMAP_9_BY_15, timStr)
      end2D()

  def display(self):
    """Frame-by-frame display function."""
    self.simulator.simulateFrame()
    glClear(GL_COLOR_BUFFER_BIT)

    self.displayBodies() # Render bodies
    self.displayData() # Show render data on screen
    
    glFlush() # Finish all drawing before this line

    # Update render data
    self.frameCount += 1
    if self.frameCount % 10 == 0:
      lastTenFramesTime = int(round(time.time() * 1000.0)) - self.frameTimeHolder
      self.avgFrameTime = lastTenFramesTime / 10000.0
      self.frameTimeHolder = int(round(time.time() * 1000.0)) 



def begin2D():
  """Allow for drawing on the screen instead of in the universe."""
  glMatrixMode(GL_PROJECTION)
  glPushMatrix()
  glLoadIdentity()
  glOrtho(0, 1000, 0, 1000, 0, 1)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

def end2D():
  """Go back to 3D mode."""
  glMatrixMode(GL_PROJECTION)
  glPopMatrix()
  orientCamera()