import math, time, numpy

from numpy import *

def equals(body, other):
    return (body==other).all()

def forceOn(body, other):
    """
    Returns the force on self by other as a vector in the direction
    self --> other
    """
    force = numpy.zeros(3)
    GRAVITATIONAL_CONSTANT = 6.67384e-11
    r = numpy.array([other[0] - body[0], other[1] - body[1], other[2] - body[2]])
    d = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
    f = (GRAVITATIONAL_CONSTANT * body[3] * other[3]) / (d**2)
    return f * (r / d)
    
def totalForceOn(body, bodies):
    """
    Calculates the total force on self from all bodies in bodies except for 
    self
    """
    total = numpy.zeros(3)
    for row in bodies:
        if not equals(body,row):
            total += forceOn(body, row)
    return total

def move(body, force, time):
    acceleration = force / body[3]
    body[4] += (acceleration[0] * time)
    body[5] += (acceleration[1] * time)
    body[6] += (acceleration[2] * time)

    body[0] += (body[4] * time)
    body[1] += (body[5] * time)
    body[2] += (body[6] * time)

def energy(body):
    return 0.5 * body[3] * math.sqrt(body[4]**2 + body[5]**2 + body[6]**2)**2
