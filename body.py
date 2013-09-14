import math

from numpy import *

def equals(body, other):
    return (body[0] == other[0] and body[1] == other[1] 
        and body[2] == other[2] and body[3] == other[3] 
        and body[4] == other[4] and body[5] == other[5] 
        and body[6] == other[6])

def forceOn(body, other):
    """
    Returns the force on self by other as a vector in the direction
    self --> other
    """
    G = 6.674e-11
    d = math.sqrt((other[0] - body[0])**2 + (other[1] - body[1])**2 + (other[2] - body[2])**2)
    f = (G * body[3] * other[3]) / (d**2)
    return f
    
def totalForceOn(body, bodies):
    """
    Calculates the total force on self from all bodies in bodies except for 
    self
    """
    total = zeros(3)
    for row in bodies:
        if not equals(body,row):
            force = forceOn(body,row)
            total[0] = total[0] + force[0]
            total[1] = total[1] + force[1]
            total[2] = total[2] + force[2]
    return total

def move(body, force, time):
    deltaV = force / body[3]
    body[4] = body[4] + deltaV[0]
    body[5] = body[5] + deltaV[1]
    body[6] = body[6] + deltaV[2]

    body[0] += (body[4] * time)
    body[1] += (body[5] * time)
    body[2] += (body[6] * time)
