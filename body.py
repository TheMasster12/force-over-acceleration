import vector

#This class will represent a point-particle and all the goodness therein
class Body(object):
  """
  Body encapsulates a body in space, which has attributes:
  position vector: <x,y,z>
  mass: m
  velocity vector: v
  """

  def __init__(self,x,y,z,m,v):
    self.x = x
    self.y = y
    self.z = z
    self.mass = m
    self.velocity = v # should be a Vector

  def __str__(self):
    return ("Body at:(" + 
            str(self.x) + ", " + 
            str(self.y) + ", " + 
            str(self.z) + ")" + 
            " with mass: " + str(self.mass))

  def __eq__(self,other):
    return (isinstance (other, self.__class__) and
            self.x == other.x and
            self.y == other.y and
            self.z == other.z and
            self.mass == other.mass and
            self.velocity == other.velocity)

  def __ne__(self,other):
    return not self.__eq__(other)
  
  def forceOn(self,other):
    """
    Returns the force on self by other as a vector in the direction
    self --> other
    """
    G = 6.674e-11
    r = self.vectorTo(other)
    d = r.length()
    F = G * self.mass * other.mass / (d*d*d)
    return r.scale(F)
  
  def totalForceOn(self, bodies):
    """
    Calculates the total force on self from all bodies in bodies except for 
    self
    """
    F = vector.zero()
    for b in bodies:
      if b != self:
        F = vector.add(F, self.forceOn(b))
    return F

  def move(self, force, time):
    deltaV = force.scale(1.0/self.mass)
    self.velocity = vector.add(self.velocity, deltaV)
    self.x += (self.velocity.x * time)
    self.y += (self.velocity.y * time)
    self.z += (self.velocity.z * time)

  def vectorTo(self,other):
    return vector.Vector(other.x-self.x, other.y-self.y, other.z-self.z)

def distance(p1,p2):
  x = p1.x - p2.x
  y = p1.y - p2.y
  z = p1.z - p2.z
  return math.sqrt (x*x + y*y + z*z)

