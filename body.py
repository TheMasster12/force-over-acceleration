import vector

CYCLE_TIME = 1e-3 #1 millisecond

#This class will represent a point-particle and all the goodness therein
class Body(object):

  def __init__(self,x,y,z,m,v):
    self.x = x
    self.y = y
    self.z = z
    self.mass = m
    self.velocity = v # should be a Vector

  def __str__(self):
    return ("Body at:(" + self.x + ", " + self.y + ", " + self.z + ")"
            + " with mass: " + self.mass)
  
  def forceOn(self,other):
    G = 6.674e-11
    r = self.vectorTo(other)
    d = r.length()
    F = G * self.mass * other.mass / (d*d)
    return r.normalize().scale(F)
  
  def interactWith(self,other):
    accel = self.forceOn(other).scale(1/self.m).scale(CYCLE_TIME)
    self.velocity = vector.add(self.velocity, accel)
    self.x += (self.velocity.x * CYCLE_TIME)
    self.y += (self.velocity.y * CYCLE_TIME)
    self.z += (Self.velocity.z * CYCLE_TIME)

  def vectorTo(self,other):
    return vector.Vector(other.x-self.x, other.y-self.y, other.z-self.z)

def distance(p1,p2):
  x = p1.x - p2.x
  y = p1.y - p2.y
  z = p1.z - p2.z
  return math.sqrt (x*x + y*y + z*z)

