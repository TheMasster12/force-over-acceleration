import math
import particle

class Vector(object):

  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  
  def length(self):
    return math.sqrt(x*x + y*y + z*z)

  def __str__(self):
    return "<" + self.x + ", " + self.y + ", " + self.z + ">"

def distance(p1,p2):
  x = p1.x - p2.x
  y = p1.y - p2.y
  z = p1.z - p2.z
  return math.sqrt (x*x + y*y + z*z)

def toVector(part):
  return vector(part.x, part.y, part.z)
