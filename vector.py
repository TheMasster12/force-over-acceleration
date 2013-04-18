import math
import body

class Vector(object):

  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
    return self

  def __str__(self):
    return "<" + self.x + ", " + self.y + ", " + self.z + ">"
  
  def length(self):
    return math.sqrt(x*x + y*y + z*z)
  
  def scale(self,c):
    self.x *= c
    self.y *= c
    self.z *= c
    return self
  
  def normalize(self):
    self.x *= self.length()
    self.y *= self.length()
    self.z *= self.length()
    return self

def toVector(b):
  return vector(b.x, b.y, b.z)
