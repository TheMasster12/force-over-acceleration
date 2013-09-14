#This class will be the backbone of the whole simulation.
import sys
import random,math, time
import body,vector,display

from numpy import *

NUM_BODIES = 100
DIM_X = 2000
DIM_Y = 2000
DIM_Z = 2000
MASS_MIN = 1e14
MASS_MAX = 1e16
VELOCITY_MIN = -1e4
VELOCITY_MAX = 1e4
PI = math.pi

class Simulator(object):

  def __init__(self):
    self.renderEngine = display.Display(self)
    self.argHolder = []
    self.bodyArray = array([])

  def generateRandomBodies(self):
    """Generates NUM_BODIES new random bodies."""
    for x in range(0,self.bodyArray.shape[0]):
      self.bodyArray[x] = self.getRandomBody()

  def removeBody(self):
    """Randomly selects a body and removes it from the bodyArray."""
    if self.bodyArray.shape[0] > 0:
      self.bodyArray = delete(self.bodyArray,random.randint(0,self.bodyArray.shape[0]),0)

  def readBodies(self,args):
    """Goes through args and reads each body into bodyArray."""
    self.bodyArray = zeros((0,7))
    for arg in args:
      b = [float(x) for x in arg.split()] # List of numbers that identify body
      self.bodyArray = vstack([self.bodyArray,b])

  def refreshBodyArray(self):
    """Resets bodyArray to initial conditions."""
    self.bodyArray = zeros((NUM_BODIES,7))

    if len(sys.argv) < 2:
      self.generateRandomBodies()
    else:
      self.readBodies(argHolder)

  def addRandomBody(self):
    self.bodyArray = vstack([self.bodyArray,getRandomBody()])

  def barycenter(self):
    """Finds the center of mass of all the bodies in the universe."""
    vs = [vector.Vector(b[0],b[1],b[2]).scale(b[3]) for b in self.bodyArray]
    totalMass = sum([b[3] for b in self.bodyArray])
    x = reduce(vector.add, vs)
    return x.scale(1.0/totalMass)

  def simulateFrame(self): 
    """Takes one step in the simulation if it isn't paused."""
    if not self.renderEngine.isPaused:
      forces = [body.totalForceOn(row,self.bodyArray) for row in self.bodyArray]
      for i in xrange(self.bodyArray.shape[0]):
        body.move(self.bodyArray[i],forces[i],self.renderEngine.avgFrameTime)

  def restartSimulation(self):
    self.renderEngine.frameCount = 0
    self.renderEngine.avgFrameTime = 0
    self.renderEngine.frameTimeHolder = int(round(time.time() * 1000.0))
    self.renderEngine.startTime = time.time()

    self.renderEngine.rho = max([DIM_X, DIM_Y, DIM_Z]) * 1.5
    self.renderEngine.theta = 0.0
    self.renderEngine.phi = PI / 2
    self.renderEngine.orientCamera()

    self.refreshBodyArray()

  def handleKeypress(self,key,x,y):
    if key == 'q':
      sys.exit(0)

    if key == 'r':
      self.restartSimulation()

    if key == 'f':
      self.renderEngine.showData = not self.renderEngine.showData

    if key == 'p':
      self.renderEngine.isPaused = not self.renderEngine.isPaused

    if key == 'n':
      self.addRandomBody()

    if key == 'd':
      self.removeBody()

  def handleSpecial(self,key,x,y):
    MOVE_SPEED = .03

    if key == GLUT_KEY_UP:
      if self.renderEngine.phi > MOVE_SPEED:
        self.renderEngine.phi -= MOVE_SPEED

    if key == GLUT_KEY_DOWN:
      if self.renderEngine.phi < PI-MOVE_SPEED:
        self.renderEngine.phi += MOVE_SPEED

    if key == GLUT_KEY_LEFT:
      self.renderEngine.theta -= MOVE_SPEED

    if key == GLUT_KEY_RIGHT:
      self.renderEngine.theta += MOVE_SPEED

    self.renderEngine.orientCamera()

  def handleMouse(self,button, state, x, y):
    if button == 3:
      if state == GLUT_DOWN:
        if self.renderEngine.rho > 200: self.renderEngine.rho -= 200
        self.renderEngine.orientCamera()
    if button == 4:
      if state == GLUT_DOWN:
        self.renderEngine.rho += 200
        self.renderEngine.orientCamera()

  def getRandomBody(self):
    """Returns a random body."""
    ranX = random.random() * DIM_X - (DIM_X / 2)
    ranY = random.random() * DIM_Y - (DIM_Y / 2)
    ranZ = random.random() * DIM_Z - (DIM_Z / 2)
    ranMass = random.uniform(MASS_MIN,MASS_MAX)
    
    #ranVx = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    #ranVy = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    #ranVz = random.uniform(VELOCITY_MIN,VELOCITY_MAX)
    ranVx = 0.0
    ranVy = 0.0
    ranVz = 0.0

    return [ranX,ranY,ranZ,ranMass,ranVx,ranVy,ranVz]
    
