import vector

def equals(body,other):
  return (body[0] == other[0] and body[1] == other[1] 
    and body[2] == other[2] and body[3] == other[3] 
    and body[4] == other[4] and body[5] == other[5] 
    and body[6] == other[6])

def forceOn(body,other):
  """
  Returns the force on self by other as a vector in the direction
  self --> other
  """
  G = 6.674e-11
  r = vectorTo(body,other)
  d = r.length()
  F = G * body[3] * other[3] / (d*d*d)
  return r.scale(F)
  
def totalForceOn(body, bodies):
  """
  Calculates the total force on self from all bodies in bodies except for 
  self
  """
  F = vector.zero()
  for row in bodies:
    if not equals(body,row):
      F = vector.add(F, forceOn(body, row))
  return F

def move(body, force, time):
  deltaV = force.scale(1.0/body[3])
  V = vector.add(vector.Vector(body[4],body[5],body[6]), deltaV)
  body[4] = V.x
  body[5] = V.y
  body[6] = V.z

  body[0] += (body[4] * time)
  body[1] += (body[5] * time)
  body[2] += (body[6] * time)

def vectorTo(body,other):
    return vector.Vector(other[0]-body[0], other[1]-body[1], other[2]-body[2])

def distance(p1,p2):
  x = p1.x - p2.x
  y = p1.y - p2.y
  z = p1.z - p2.z
  return math.sqrt (x*x + y*y + z*z)

