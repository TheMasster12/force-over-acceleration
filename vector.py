import math
import body

class Vector(object):
  """
  Vector encapsulates a vector which has x,y,z coordinates
  """

  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    return ("<" + str(self.x) + ", " + 
                  str(self.y) + ", " +
                  str(self.z) + ">")
  
  def __eq__(self,other):
    return (isinstance (other, self.__class__) and
            self.x == other.x and
            self.y == other.y and
            self.z == other.z)

  def __ne__(self,other):
    return not self.__eq__(other)

  def length(self):
    return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
  
  def scale(self,c):
    """
    Scales self by the scalar c
    """
    self.x *= c
    self.y *= c
    self.z *= c
    return self
  
  def normalize(self):
    """
    Alters self so that it has length 1
    """
    self.x /= self.length()
    self.y /= self.length()
    self.z /= self.length()
    return self

def zero():
  return Vector(0,0,0)

def toVector(b):
  return Vector(b.x, b.y, b.z)

def add(v1,v2):
  """
  Add vectors v1 and v2
  """
  return Vector(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)

# Dot product of v1 and v2
def dotprod(v1,v2):
  """
  Dot product of vectors v1 and v2
  """
  return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
