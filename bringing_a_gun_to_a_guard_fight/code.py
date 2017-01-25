import math

dim = [3, 2]
gPos = [1, 1]
bPos = [2, 1]

WALL_N = 0
WALL_S = 1
WALL_E = 2
WALL_W = 3

def howOff(b, walls, subOrAdd):
    reflections = len(walls) - 1
    numer = dim[1] - gPos[1]
    denom = howOffRec(b, walls, subOrAdd, 0) - gPos[0]
    lhs = math.atan(abs(numer/denom))
    return lhs - (math.pi / 2 - b)

def howOffRec(b, walls, subOrAdd, i):
    i += 1
    if len(walls) > 0:
        # print(posOfWall(walls[0]))
        # print('-')
        # print(abs(posOfWall(walls[1])) - howOffRec(math.pi / 2 - b, walls))
        # print('/')
        # print(math.tan(math.pi / 2 - b))
        # print(b, walls)

        v = subOrAdd.pop()
        w = walls.pop()
        x = walls.pop()
        y = howOffRec(math.pi / 2 - b, walls, subOrAdd, i)
        z = math.tan(math.pi / 2 - b)

        print(str(w) + ' + ' + str(v) + ' * abs(' + str(x) + ' - ' + str(y) + ') / ' + str(z) + ' = ' + str(w + v * abs(x - y) / z))

        return w + v * abs(x - y) / z
    else:
        return bPos[0]

def posOfWall(wall):
    if wall is WALL_N:
        return dim[1]
    elif wall is WALL_E:
        return dim[0]
    else:
        return 0

def eq(a, b):
    return (abs(a - b) < 0.00000001)

print(howOff(math.atan(3.0/2.0),
    [posOfWall(WALL_E),
    bPos[1],
    posOfWall(WALL_N),
    posOfWall(WALL_E)],
    [1, -1]))

def answer():

    return 0
