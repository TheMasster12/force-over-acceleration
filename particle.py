import vectors

#This class will represent a point-particle and all the goodness therein
class Particle(object):

  def __init__(self,x,y,z,m,v):
    self.x = x
    self.y = y
    self.z = z
    self.mass = m
    self.velocity = v # should be a Vector

  def kineticEnergy():
    return 0.5 * self.mass * self.velocity.length() * self.velocity.length()
