import math

def answer(n):
    return q(n) - 1

# return the nth pentagonal number, p, where
# p = (3n^2 - n) / 2   for n >= 1
def pentagonalNumber(n):
    return int(n * (3 * n - 1) / 2.0)

# solve k = 3m^2 - m for m using the quadratic formula
# only return integer results work for this formula
def calcM(k):
    try:
        m = (1 + math.sqrt(1 + 12 * k)) / 6
        if m.is_integer():
            return m
    except ValueError:
        pass # square root of negative number is undefined
    try:
        m = (1 - math.sqrt(1 + 12 * k)) / 6
        if m.is_integer():
            return m
    except ValueError:
        pass # square root of negative number is undefined
    return None

# solve for q: the number of partitions of k with distinct parts
# using dynamic programming and recursion
# q(k) = ak + q(k - 1) + q(k - 2) - q(k - 5) - q(k - 7) + q(k - 12) + ...
qCache = {}
def q(k):
    # DP: return if already calculated
    if k in qCache:
        return qCache[k]

    # calculate m: some integer where k = 3m^2 - m
    m = calcM(k)
    if m is not None:
        ak = 1 if m % 2 == 0 else -1
    else:
        ak = 0

    theSum = ak
    i = 0
    while True:
        signMult = 1
        if (i / 2) % 2 != 0:
            signMult = -1
        pn = pentagonalNumber((i / 2 + 1) * (-1 if i % 2 != 0 else 1))
        if k - pn < 0:
            break
        theSum += signMult * q(k - pn)
        i += 1

    qCache[k] = theSum
    return theSum
