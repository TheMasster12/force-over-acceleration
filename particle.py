#This class will represent a point-particle and all the goodness therein
class Particle(object):

   def __init__(self,x,y,z,m,v):
      self.x = x
      self.y = y
      self.z = z
      self.mass = m
      self.velocity = v

   def getKineticEnergy():
     return 0.5 * self.mass * self.velocity * self.velocity
