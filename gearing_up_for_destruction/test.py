# This one was actually a really interesting problem.
# Brute-force is too slow, so fancy math had to be done.

from fractions import Fraction

# calcRadius calculates the first gear's size as a fraction, or
# ( -2     4        n )   (               n-1      n-1                  i  )
# ( --- + --- * (-1)  ) * ( p   + p * (-1)  +2*(-1)*sum(i=1,n-2,p * (-1) ) )
# (  3     3          )   (  n-1   0                             i         )
# where p = pegs & n = number of gears = len(pegs)
def calcRadius(pegs):
    lastInd = len(pegs) - 1
    evenOdd = 1 if len(pegs) % 2 == 0 else -1 # 1 if even, -1 if odd

    mult = 0
    for i in range(1, lastInd):
        mult += pegs[i] * (1 if i % 2 == 0 else -1)
    mult *= 2 * (-1 * evenOdd)
    mult += pegs[lastInd] + (-1 * evenOdd) * pegs[0]
    mult *= Fraction(-2 + 4 * evenOdd, 3)
    return mult

# friendly wrapper for calcRadiiRec
def calcRadii(pegs, a, b):
    return calcRadiiRec(pegs, a, b, [a / b])

# calculate and return radii of gears recursively
# precondition: radii must be a list == [a/b]
def calcRadiiRec(pegs, a, b, radii):
    if len(radii) >= len(pegs):
        return radii
    else:
        index = len(radii)
        radii.append(pegs[index] - pegs[index - 1] - radii[index - 1])
        return calcRadiiRec(pegs, a, b, radii)

# return true if radii are all valid (that is, each radius >= 1)
def radiiAreValid(radii):
    for radius in radii:
        if radius < 1:
            return False
    return True

def answer(pegs):
    if len(pegs) < 2:
        return [-1, -1]

    # find valid [a, b] values for first gear's ratio, a/b
    radius = calcRadius(pegs)
    if radius <= 1:
        return [-1, -1]

    # now, with a valid first gear, ensure all gear sizes are valid
    a = radius.numerator
    b = radius.denominator
    radii = calcRadii(pegs, a, b)
    if radiiAreValid(radii):
        return [a, b]
    else:
        return [-1, -1]
