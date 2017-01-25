# the variables were assigned clockwise
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

TEST_A = [[0, 1, 1, 0],
          [0, 0, 0, 1],
          [1, 1, 0, 0],
          [1, 1, 1, 0]]
ANS_A = 7

TEST_B = [[0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]]
ANS_B = 11

TEST_C = [[0, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0]]
ANS_C = 11

TEST_D = [[0, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 0]]
ANS_D = 11

TEST_E = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
          [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
          [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
ANS_E = 25

TEST_F = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
          [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
          [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
          [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
          [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0]]


TEST_G = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
          [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
          [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
          [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
          [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
          [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
          [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
          [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
          [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]]


TEST_H = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
          [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
          [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
          [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
          [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
          [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0]]


TEST_I = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
          [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
          [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
          [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]]

TEST_K = [[0, 0, 0, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

changedX = 0
changedY = 0

def printMatrixB(matrix, blank):
    strOut = ''
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value in blank:
                strOut += '   '
            else:
                strOut += ' ' + str(value).rjust(2)
        strOut += '\n' if row < len(matrix) - 1 else ''
    print(strOut)
    return strOut

def printMatrix(matrix):
    return printMatrixB(matrix, [])

def isOpen(maze, x, y):
    try:
        if x >= 0 and y >= 0:
            return maze[y][x] == 0
        else:
            return False
    except IndexError:
        # outside of maze, so not an open spot
        return False

def recShortestPath(maze, x, y, sizes, curSize, fromDir):
    # print(' '*curSize + '[' + str(x) + ', ' + str(y) + ']')
    # strOut = ''
    # for row in range(len(maze)):
    #     for col in range(len(maze[row])):
    #         if row == y and col == x:
    #             strOut += ' x'
    #         else:
    #             strOut += ' ' + str(maze[row][col])
    #     strOut += '\n'
    # print(strOut)
    # input('')

    if curSize < sizes[0]:
        if y == len(maze) - 1 and x == len(maze[0]) - 1:
            if curSize not in sizes:
                sizes.append(curSize)
                sizes.sort()
                # print(sizes)
        else:
            if (fromDir != RIGHT and isOpen(maze, x + 1, y)):
                # if x + 1 > 1: print(x + 1)
                recShortestPath(maze, x + 1, y, sizes, curSize + 1, LEFT)
            if (fromDir != DOWN and isOpen(maze, x, y + 1)):
                recShortestPath(maze, x, y + 1, sizes, curSize + 1, UP)
            if (fromDir != UP and isOpen(maze, x, y - 1)):
                recShortestPath(maze, x, y - 1, sizes, curSize + 1, DOWN)
            if (fromDir != LEFT and isOpen(maze, x - 1, y)):
                recShortestPath(maze, x - 1, y, sizes, curSize + 1, RIGHT)

def calcShortestPathLength(maze):
    sizes = [len(maze) * len(maze)]
    recShortestPath(maze, 0, 0, sizes, 1, UP)
    return sizes[0]

def openingWasCreated(maze, x, y):
    # (x, y) will be 0. Check if an opening was made as a result
    # check straight paths
    if x != 0 and x != len(maze[0]) - 1:
        if maze[y][x + 1] == maze[y][x - 1] == 0:
            return True
    if y != 0 and y != len(maze) - 1:
        if maze[y + 1][x] == maze[y - 1][x] == 0:
            return True
    # check corner paths
    if x != 0 and y != 0:
        if maze[y - 1][x] == maze[y][x - 1] == 0:
            return True
    if x != len(maze[0]) - 1 and y != 0:
        if maze[y - 1][x] == maze[y][x + 1] == 0:
            return True
    if x != 0 and y != len(maze) - 1:
        if maze[y + 1][x] == maze[y][x - 1] == 0:
            return True
    if x != len(maze[0]) - 1 and y != len(maze) - 1:
        if maze[y + 1][x] == maze[y][x + 1] == 0:
            return True
    return False

def recCalcPathMinDistances(maze, distMatrix, x, y, curDist, toX, toY):
    # stop if
    #  hit end
    #  hit 1
    # hit something filled in already
    #  which is min? that's the new
    #  if this is min, set it.
    #  else, stop
    # print(distMatrix)
    if x < 0 or y < 0 or x >= len(maze[0]) or y >= len(maze):
        return False
    if maze[y][x] == 1:
        return False
    if distMatrix[y][x] != 0 and curDist >= distMatrix[y][x]:
        return False
    # if addOrSub == -1 and curDist < distMatrix[y][x]:
    #     return False

    # no stop? great, do stuff and rec part
    # do stuff: set minDist to value
    distMatrix[y][x] = curDist

    # if x == toX and y == toY:
        # addOrSub = -1
        # return True
    # rec part: try all four directions with value + 1
    curDist += 1
    # if addOrSub == -1:
    #     printMatrix(distMatrix)
    #     input()
    c = recCalcPathMinDistances(maze, distMatrix, x - 1, y, curDist, toX, toY)
    d = recCalcPathMinDistances(maze, distMatrix, x, y - 1, curDist, toX, toY)
    a = recCalcPathMinDistances(maze, distMatrix, x + 1, y, curDist, toX, toY)
    b = recCalcPathMinDistances(maze, distMatrix, x, y + 1, curDist, toX, toY)
    curDist -= 1
    if a == b == c == d == False:
        return False
    else:
        return True

def calcPathMinDistancesFrom(maze, fromX, fromY, toX, toY):
    endX = len(maze[0]) - 1
    endY = len(maze) - 1
    distMatrix = [ [0]*(endX + 1) for _ in range(endY + 1) ]
    if recCalcPathMinDistances(maze, distMatrix, fromX, fromY, 1, toX, toY) or True:
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == 1:
                    distMatrix[row][col] = -1
        return distMatrix
    else:
        # printMatrix(distMatrix)
        return [[distMatrix[toY][toX]]]

def foobar(distMatrixFromStart, distMatrixFromEnd, x1, y1, x2, y2, pathDistMatrix):
    start1 = distMatrixFromStart[y1][x1]
    start2 = distMatrixFromStart[y2][x2]
    end1 = distMatrixFromEnd[y1][x1]
    end2 = distMatrixFromEnd[y2][x2]
    # print(distMatrixFromStart)
    # print(distMatrixFromEnd)
    if start1 != -1 and start2 != -1 and start1 != 0 and start2 != 0:
        # print(str(startX) + ' - ' + str(startY) + ' ?= ' + str(endY) + ' - ' + str(endX) + ' == ' + str(startX - startY))
        a = abs(start1 - start2)
        b = abs(end2 - end1)
        if a + b > 0:
            # print('[' + str(a + b) + ', ' + str(min(a, b) - 2) + ']')
            pathDist = pathDistMatrix[y1][x1] + pathDistMatrix[y2][x2]
            if x1 == 16 and y1 == 7:
                print('----------------')
                print(a)
                print(b)
                print(pathDist)
            return [a + b - pathDist, min(a, b) - 2 - min(pathDistMatrix[y1][x1], pathDistMatrix[y2][x2])]
    return [0, 0]

def calcCutDist(distMatrixStart, distMatrixEnd, x, y, pathDistMatrix):
    maxX = len(distMatrixStart[0]) - 1
    maxY = len(distMatrixStart) - 1
    # try all arrangements, return greatest dist cut
    distCutRanks = [0]*6
    distCuts = [0]*6
    if x > 0 and x < maxX: # horizontal opening
        distCutRanks[0], distCuts[0] = foobar(distMatrixStart, distMatrixEnd, x - 1, y, x + 1, y, pathDistMatrix)
    if y > 0 and y < maxY: # vertical opening
        distCutRanks[1], distCuts[1] = foobar(distMatrixStart, distMatrixEnd, x, y - 1, x, y + 1, pathDistMatrix)
    if x > 0 and y > 0: # top-left opening
        distCutRanks[2], distCuts[2] = foobar(distMatrixStart, distMatrixEnd, x - 1, y, x, y - 1, pathDistMatrix)
    if x < maxX and y > 0: # top-right opening
        distCutRanks[3], distCuts[3] = foobar(distMatrixStart, distMatrixEnd, x + 1, y, x, y - 1, pathDistMatrix)
    if x > 0 and y < maxY: # bottom-left opening
        distCutRanks[4], distCuts[4] = foobar(distMatrixStart, distMatrixEnd, x - 1, y, x, y + 1, pathDistMatrix)
    if x < maxX and y < maxY: # bottom-right opening
        distCutRanks[5], distCuts[5] = foobar(distMatrixStart, distMatrixEnd, x + 1, y, x, y + 1, pathDistMatrix)

    # return max distance cut value
    # x = distCutRanks.index(max(distCutRanks))
    return distCuts[distCutRanks.index(max(distCutRanks))]
    # return distCuts[-1]

def calcBiggestDistCut(distMatrixFromStart, distMatrixFromEnd, pathDistMatrix):
    maxCut = 0
    maxX = 0
    maxY = 0
    for row in range(len(distMatrixFromStart)):
        for col in range(len(distMatrixFromStart[row])):
            if distMatrixFromStart[row][col] == -1:
                oldMC = maxCut
                maxCut = max(calcCutDist(distMatrixFromStart, distMatrixFromEnd, col, row, pathDistMatrix), maxCut)
                if oldMC < maxCut:
                    maxX = col
                    maxY = row

    print('removed wall at: (' + str(maxX) + ', ' + str(maxY) + ')')
    global changedX
    global changedY
    changedX = maxX
    changedY = maxY
    return maxCut

def recOptimalPaths(matrix, path):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    if path[-1] == [width, height]:
        return True

    # check all adjacent spots to last spot in path
    x = path[-1][0]
    y = path[-1][1]

    # if any one is exactly one greater, it's a part of the path
    # add to path
    # see how far the rabbit hole goes
    a = b = c = d = False
    try:
        if matrix[y][x] + 1 == matrix[y][x + 1]:
            path.append([x + 1, y])
            a = recOptimalPaths(matrix, path)
            if not a:
                path.remove([x + 1, y])
    except IndexError:
        pass # out of range
    try:
        if matrix[y][x] + 1 == matrix[y][x - 1]:
            path.append([x - 1, y])
            b = recOptimalPaths(matrix, path)
            if not b:
                path.remove([x - 1, y])
    except IndexError:
        pass # out of range
    try:
        if matrix[y][x] + 1 == matrix[y + 1][x]:
            path.append([x, y + 1])
            c = recOptimalPaths(matrix, path)
            if not c:
                path.remove([x, y + 1])
    except IndexError:
        pass # out of range
    try:
        if matrix[y][x] + 1 == matrix[y - 1][x]:
            path.append([x, y - 1])
            d = recOptimalPaths(matrix, path)
            if not d:
                path.remove([x, y - 1])
    except IndexError:
        pass # out of range
    if a == b == c == d == False:
        return False
    return True

def optimalPaths(distMatrixFromStart):
    path = [[0, 0]]
    if recOptimalPaths(distMatrixFromStart, path):
        uniquePath = []
        for i in path:
            if i not in uniquePath:
                uniquePath.append(i)
        return uniquePath
    else:
        return []

def recDistFromPath(maze, path, x, y, dist, minDistMatrix):
    dist += 1
    nextSpots = [[x, y + 1],
                 [x, y - 1],
                 [x + 1, y],
                 [x - 1, y]]
    validSpots = []
    for coords in nextSpots:
        x = coords[0]
        y = coords[1]
        if [x, y] in path:
            return dist
        if x < 0 or y < 0:
            continue
        try:
            if maze[y][x] == -1:
                continue
        except IndexError:
            continue
        if dist < minDistMatrix[y][x] or minDistMatrix[y][x] == -1:
            minDistMatrix[y][x] = dist
            # okay to continue recursion
            validSpots.append(coords)
    recResults = []
    for coords in validSpots:
        x = coords[0]
        y = coords[1]
        recResults.append(recDistFromPath(maze, path, x, y, dist, minDistMatrix))

    if len(recResults) == 0:
        return -1
    for result in recResults:
        if result != -1:
            return result
    return -1
    # crawl away from x, y, keeping track of dist
    # as soon as a point from path is hit, return dist
    # print('(' + str(x) + ', ' + str(y) + ') - ' + str(dist))
    # input()
    # if y < 0 or x < 0:
    #     return -1
    # try:
    #     if maze[y][x] == 1:
    #         return -1
    # except IndexError: # outside of maze, not a valid spot
    #     return -1
    # if dist > 2 * len(maze):
    #     return -1
    #
    # if dist >= minDistMatrix[y][x] or minDistMatrix[y][x] != -1:
    #     return -1
    # else:
    #     minDistMatrix[y][x] = dist
    #
    # if [x, y] in path:
    #     return dist
    # else:
    #     returnList = []
    #     a = recDistFromPath(maze, path, x + 1, y, dist + 1, minDistMatrix)
    #     if a != -1:
    #         returnList.append(a)
    #     b = recDistFromPath(maze, path, x - 1, y, dist + 1, minDistMatrix)
    #     if b != -1:
    #         returnList.append(b)
    #     c = recDistFromPath(maze, path, x, y + 1, dist + 1, minDistMatrix)
    #     if c != -1:
    #         returnList.append(c)
    #     d = recDistFromPath(maze, path, x, y - 1, dist + 1, minDistMatrix)
    #     if d != -1:
    #         returnList.append(d)
    #     if len(returnList) > 0:
    #         return min(returnList)
    # return -1

def distFromPath(maze, path, x, y):
    distMatrix = [ [-1]*(len(maze[0]) + 1) for _ in range(len(maze) + 1) ]
    dist = recDistFromPath(maze, path, x, y, 0, distMatrix)
    return dist

def recCalcDistFromPathSpot(maze, path, x, y, pathDistMatrix, dist):
    dist += 1
    nextSpots = [[x, y + 1],
                 [x, y - 1],
                 [x + 1, y],
                 [x - 1, y]]
    for coords in nextSpots:
        x = coords[0]
        y = coords[1]
        if [x, y] in path:
            continue
        if x < 0 or y < 0:
            continue
        try:
            if maze[y][x] == 1:
                continue
        except IndexError:
            continue
        if dist < pathDistMatrix[y][x] or pathDistMatrix[y][x] == -1:
            pathDistMatrix[y][x] = dist
            # okay to continue recursion
            recCalcDistFromPathSpot(maze, path, x, y, pathDistMatrix, dist)

def calcDistFromPathMatrix(maze, path):
    pathDistMatrix = [ [-1]*(len(maze[0]) + 1) for _ in range(len(maze) + 1) ]
    for i in path:
        recCalcDistFromPathSpot(maze, path, i[0], i[1], pathDistMatrix, 0)
        pathDistMatrix[i[1]][i[0]] = 0
    return pathDistMatrix

distMatrixA = []
distMatrixB = []
path = []
pathDistMatrix = []
cutMatrix = []

def printCandidacy(maze):
    global distMatrixA
    global distMatrixB
    global path
    global pathDistMatrix
    global cutMatrix

    maxX = len(maze[0]) - 1
    maxY = len(maze) - 1
    distMatrixA = calcPathMinDistancesFrom(maze, maxX, maxY, 0, 0)
    distMatrixB = calcPathMinDistancesFrom(maze, 0, 0, maxX, maxY)
    path = optimalPaths(distMatrixB)
    pathDistMatrix = calcDistFromPathMatrix(maze, path)

    cutMatrix = [ [-1]*(len(maze[0]) + 1) for _ in range(len(maze) + 1) ]
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                cutMatrix[row][col] = calcCutDist(distMatrixA, distMatrixB, col, row, pathDistMatrix)
            if [col, row] in path:
                cutMatrix[row][col] = 'X'
    printMatrix(maze)
    print('---------------------------')
    printMatrixB(cutMatrix, [-1])

def a(maze): # the maze walls, start, and end
    h = len(maze) - 1
    w = len(maze[0]) - 1
    maze[0][0] = 'X'
    maze[h][w] = 'X'
    printMatrixB(maze, [0])
    maze[0][0] = 0
    maze[h][w] = 0
import copy
def b(maze): # the optimal path
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromStart = calcPathMinDistancesFrom(maze, 0, 0, w, h)
    path = optimalPaths(distMatrixFromStart)
    pathedMaze = copy.deepcopy(maze)
    for row in range(h + 1):
        for col in range(w + 1):
            if maze[row][col] == 1:
                pathedMaze[row][col] = 1
            else:
                if [col, row] in path:
                    pathedMaze[row][col] = 'X'
                else:
                    pathedMaze[row][col] = -1
    printMatrixB(pathedMaze, [-1])
def c(maze): # the minimum distance of each point from the path
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromStart = calcPathMinDistancesFrom(maze, 0, 0, w, h)
    path = optimalPaths(distMatrixFromStart)
    minFromPath = calcDistFromPathMatrix(maze, path)
    printMatrixB(minFromPath, [-1])
def d(maze): # the minimum distance of each point from the start
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromStart = calcPathMinDistancesFrom(maze, 0, 0, w, h)
    printMatrixB(distMatrixFromStart, [-1])
def e(maze): # the minimum distance of each point from the end
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromEnd = calcPathMinDistancesFrom(maze, w, h, 0, 0)
    printMatrixB(distMatrixFromEnd, [-1])
def f(maze): # the minimum distance of each point from either the start or end
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromStart = calcPathMinDistancesFrom(maze, 0, 0, w, h)
    distMatrixFromEnd = calcPathMinDistancesFrom(maze, w, h, 0, 0)
    distMatrixBoth = copy.deepcopy(maze)
    for y in xrange(h + 1):
        for x in xrange(w + 1):
            distMatrixBoth[y][x] = min(distMatrixFromStart[y][x],
                                       distMatrixFromEnd[y][x])
    printMatrixB(distMatrixBoth, [-1])
def g(maze):
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromStart = calcPathMinDistancesFrom(maze, 0, 0, w, h)
    distMatrixFromEnd = calcPathMinDistancesFrom(maze, w, h, 0, 0)
    distMatrixBoth = copy.deepcopy(maze)
    # pathDistMatrix = [ [-1]*(len(maze[0]) + 1) for _ in range(len(maze) + 1) ]
    pathLengths = set([distMatrixFromEnd[0][0]])
    for y in xrange(h + 1):
        for x in xrange(w + 1):
            if maze[y][x] == 1:
                # check each possible pathway
                paths = [[x + 1, y, x - 1, y], # horizontal
                         [x, y + 1, x, y - 1], # vertical
                         [x, y + 1, x + 1, y], # above-right corner
                         [x, y + 1, x - 1, y], # above-left corner
                         [x, y - 1, x + 1, y], # below-right corner
                         [x, y - 1, x - 1, y]] # below-left corner
                allLengths = set()
                for x1, y1, x2, y2 in paths:
                    try:
                        maze[y1][x1] + maze[y2][x2]
                        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                            continue
                    except IndexError:
                        # outside of maze
                        continue
                    if maze[y1][x1] == 0 and maze[y2][x2] == 0:
                        # is, in fact, a pathway: calculate new path length
                        distFromStart1 = distMatrixFromStart[y1][x1]
                        distFromStart2 = distMatrixFromStart[y2][x2]
                        distFromEnd1 = distMatrixFromEnd[y1][x1]
                        distFromEnd2 = distMatrixFromEnd[y2][x2]
                        if distFromStart1 > 0 and distFromStart2 > 0 and distFromEnd1 > 0 and distFromEnd2 > 0:
                            if distFromStart1 < distFromStart2:
                                length = distFromStart1 + distFromEnd2 + 1
                            else:
                                length = distFromStart2 + distFromEnd1 + 1
                            allLengths.add(length)
                if len(allLengths) > 0:
                    minPathLengthForWall = min(allLengths)
                    pathLengths.add(minPathLengthForWall)
                    distMatrixBoth[y][x] = minPathLengthForWall
    print('Original length: ' + str(distMatrixFromEnd[0][0]))
    print('Minimum length: ' + str(min(pathLengths)))
    printMatrixB(distMatrixBoth, [0])

    return min(pathLengths)
def h(maze):
    h = len(maze) - 1
    w = len(maze[0]) - 1
    distMatrixFromStart = calcPathMinDistancesFrom(maze, 0, 0, w, h)
    distMatrixFromEnd = calcPathMinDistancesFrom(maze, w, h, 0, 0)
    distMatrixBoth = copy.deepcopy(maze)
    # pathDistMatrix = [ [-1]*(len(maze[0]) + 1) for _ in range(len(maze) + 1) ]
    pathLengths = set([distMatrixFromEnd[0][0]])
    for y in xrange(h + 1):
        for x in xrange(w + 1):
            if maze[y][x] == 1:
                # check each possible pathway
                paths = [[x + 1, y, x - 1, y], # horizontal
                         [x, y + 1, x, y - 1], # vertical
                         [x, y + 1, x + 1, y], # above-right corner
                         [x, y + 1, x - 1, y], # above-left corner
                         [x, y - 1, x + 1, y], # below-right corner
                         [x, y - 1, x - 1, y]] # below-left corner
                allLengths = set()
                for x1, y1, x2, y2 in paths:
                    try:
                        maze[y1][x1] + maze[y2][x2]
                        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                            continue
                    except IndexError:
                        # outside of maze
                        continue
                    if maze[y1][x1] == 0 and maze[y2][x2] == 0:
                        # is, in fact, a pathway: calculate new path length
                        distFromStart1 = distMatrixFromStart[y1][x1]
                        distFromStart2 = distMatrixFromStart[y2][x2]
                        distFromEnd1 = distMatrixFromEnd[y1][x1]
                        distFromEnd2 = distMatrixFromEnd[y2][x2]
                        if distFromStart1 > 0 and distFromStart2 > 0 and distFromEnd1 > 0 and distFromEnd2 > 0:
                            if distFromStart1 < distFromStart2:
                                length = distFromStart1 + distFromEnd2 + 1
                            else:
                                length = distFromStart2 + distFromEnd1 + 1
                            allLengths.add(length)
                if len(allLengths) > 0:
                    minPathLengthForWall = min(allLengths)
                    pathLengths.add(minPathLengthForWall)
                    distMatrixBoth[y][x] = minPathLengthForWall

    return min(pathLengths)




def answer(maze):
    return allTimeSmallest(maze)
    # construct a matrix of shortest distance from point to exit
    # maxX = len(maze[0]) - 1
    # maxY = len(maze) - 1
    # distMatrixA = calcPathMinDistancesFrom(maze, maxX, maxY, 0, 0)
    # distMatrixB = calcPathMinDistancesFrom(maze, 0, 0, maxX, maxY)
    # printMatrix(maze)
    # print('-------------')
    # printMatrix(distMatrixA)
    # print('-------------')
    # printMatrix(distMatrixB)
    # print('-------------')
    # originalTime = distMatrixA[0][0]
    # print('originally took: ' + str(originalTime))
    # if len(distMatrixA) == 1:
    #     return originalTime
    #
    # path = optimalPaths(distMatrixB)
    # pathDistMatrix = calcDistFromPathMatrix(maze, path)
    #
    # # find which wall's destruction would cause the greatest time cut
    # distCut = calcBiggestDistCut(distMatrixA, distMatrixB, pathDistMatrix)
    # print('now takes: ' + str(distCut) + ' less')

    return g(maze)

    # global distMatrixA
    # global cutMatrix
    # printCandidacy(maze)
    # maxCut = 0
    # for i in cutMatrix:
    #     for j in i:
    #         if j != 'X':
    #             maxCut = max(maxCut, j)
    # print('maxCut = ' + str(maxCut))
    #
    # return distMatrixA[0][0] - maxCut

    # strOut = ''
    # for row in range(len(distMatrix)):
    #     for col in range(len(distMatrix[row])):
    #         if distMatrix[row][col] == 0:
    #             strOut += '  X'
    #         else:
    #             strOut += ' ' + str(distMatrix[row][col]).rjust(2)
    #     strOut += '\n' if row < len(distMatrix) - 1 else ''
    # print(strOut)

    # global changedX
    # global changedY
    # maze[changedY][changedX] = 0
    # print(changedX)
    # distMatrix = calcPathMinDistancesFrom(maze, maxX, maxY, 0, 0)
    # return distMatrix[0][0]

    # return originalTime - distCut


    #
    # minPath = calcShortestPathLength(maze)
    # # minDel = [-1, -1]
    # if len(maze) > 10: return 20
    # for row in range(len(maze)):
    #     for col in range(len(maze[0])):
    #         if maze[row][col] == 1:
    #             maze[row][col] = 0
    #             if openingWasCreated(maze, col, row):
    #                 testMin = calcShortestPathLength(maze)
    #                 # if testMin < minPath:
    #                 #     minDel = [row, col]
    #                 minPath = min(minPath, testMin)
    #             maze[row][col] = 1
    # return minPath
    # # print(minPath)
    # # print(minDel)

# print(answer(TEST_F))

import random

# def allTimeSmallestVsH(maze):
#     if h(maze) != allTimeSmallest(maze):
#         print('There is, in fact, a failing')


def distFromEnd(maze):
    w = len(maze[0]) - 1
    h = len(maze) - 1
    return calcPathMinDistancesFrom(maze, w, h, 0, 0)

def randTest():
    width = int(random.random() * 100 % (20 - 2)) + 2
    height = int(random.random() * 100 % (20 - 2)) + 2

    width = 16
    height = 16

    randMaze = [ [0]*(width) for _ in range(height) ]
    for i in xrange(len(randMaze)):
        for j in xrange(len(randMaze[i])):
            randMaze[i][j] = 1 if random.random() > .5 else 0

    # printMatrix(randMaze)

    # if is solvable
    # a = calculate length
    # add an obstacle
    # if is still solvable
    # b = calculate length when extra obstacle is present
    # if b > a, this is a failed test case
    # print out the interesting failed test case

    distMatrix = distFromEnd(randMaze)
    if distMatrix[0][0] <= 0:
        return

    if h(randMaze) == allTimeSmallest(randMaze):
        return
    else:
        print('Failing test case:')
        failureStr = printMatrix(randMaze)
        failureStr += '\n' + '-' * len(failureStr.split('\n')) + '\n'
        failureStr += printMatrix(randMaze)
        failureStr += '\n\na = ' + str(randMaze) + '\n\n\n'
        f = open('failures.txt', 'a')
        f.write(failureStr)
        f.flush()
        f.close()
        # return False

    # origRandMaze = copy.deepcopy(randMaze)
    #
    # returnValue = True
    # didTrySomething = False
    # distMatrix = distFromEnd(randMaze)
    # if distMatrix[0][0] > 0:
    #     oldLength = distMatrix[0][0]
    #     for row in xrange(len(randMaze)):
    #         for col in xrange(len(randMaze[0])):
    #             if randMaze[row][col] == 0 and row > 0 and col > 0:
    #                 randMaze[row][col] = 1
    #                 newLength = h(randMaze)
    #                 if newLength > 0:
    #                     didTrySomething = True
    #                 if newLength > oldLength:
    #                     # failed case, finally!
    #                     returnValue = False
    #                     print('Failing test case:')
    #                     failureStr = printMatrix(origRandMaze)
    #                     failureStr += '\n' + '-' * len(failureStr.split('\n')) + '\n'
    #                     failureStr += printMatrix(randMaze)
    #                     f = open('failures.txt', 'a')
    #                     failureStr += '\n\na = ' + str(origRandMaze)
    #                     failureStr += '\nb = ' + str(randMaze) + '\n\n\n'
    #                     f.write(failureStr)
    #                     f.flush()
    #                     f.close()
    #                 randMaze[row][col] = 0
    # if didTrySomething:
    #     print('Something passed the test')
    # return returnValue

def recSmallest(maze, cache, x, y, dist):
    dist += 1
    w = len(maze[0]) - 1
    h = len(maze) - 1
    if x < 0 or x > w or y < 0 or y > h:
        return
    if cache[y][x] <= dist and cache[y][x] != -1:
        return
    if maze[y][x] == 1:
        return

    cache[y][x] = dist
    # if y == h and x == w:
    #     return

    nextSteps = [[x, y + 1],
                 [x + 1, y],
                 [x, y - 1],
                 [x - 1, y]]
    for x, y in nextSteps:
        recSmallest(maze, cache, x, y, dist)

recSmallest2Cache = {}
recSmallest2CacheSeen = {}
def recSmallest2(maze, x, y, dist, lastX, lastY):
    cacheKey = str(maze) + str(x) + str(y) + str(dist) + str(lastX) + str(lastY)
    cacheKeySeen = str(maze) + str(x) + str(y)
    recSmallest2CacheSeen[cacheKeySeen] = True
    try:
        return recSmallest2Cache[cacheKey]
    except KeyError:
        # never encountered these variables before, RIP cache
        dist += 1
        w = len(maze[0]) - 1
        h = len(maze) - 1

        nextSteps = [[x, y + 1],
                     [x + 1, y],
                     [x, y - 1],
                     [x - 1, y]]

        for i in xrange(len(nextSteps) - 1, -1, -1):
            x1 = nextSteps[i][0]
            y1 = nextSteps[i][1]
            if x1 == w and y1 == h:
                return dist + 1
            if x1 == lastX and y1 == lastY:
                nextSteps.remove(nextSteps[i])
                continue
            if x1 < 0 or x1 > w or y1 < 0 or y1 > h:
                nextSteps.remove(nextSteps[i])
                continue
            if maze[y1][x1] == 1:
                nextSteps.remove(nextSteps[i])
                continue
            # print(x1, y1, dist, x, y)

            # check if hit a potential infinite loop and should stop
            cacheKeySeen = str(maze) + str(x1) + str(y1)
            if cacheKeySeen in recSmallest2CacheSeen:
                nextSteps.remove(nextSteps[i])
                continue
        print nextSteps

        for x1, y1 in nextSteps:
            value = recSmallest2(maze, x1, y1, dist, x, y)
            recSmallest2Cache[cacheKey] = value
            if value != -1:
                return value
        return -1

def smallest(maze):
    w = len(maze[0]) - 1
    h = len(maze) - 1
    cache = [ [-1] * (w + 1) for _ in xrange(h + 1) ]
    recSmallest(maze, cache, 0, 0, 0)
    # printMatrix(cache)
    if cache[h][w] > 0:
        return cache[h][w]
    else:
        return -1

def allTimeSmallest(maze):
    smallList = set()
    w = len(maze[0]) - 1
    h = len(maze) - 1
    for row in xrange(h + 1):
        for col in xrange(w + 1):
            if maze[row][col] == 1:
                maze[row][col] = 0
                smallList.add(smallest(maze))
                maze[row][col] = 1
    try:
        return min(smallList)
    except ValueError:
        return smallest(maze)

def test(maze):
    if h(maze) == allTimeSmallest(maze):
        return True
    else:
        return False


'''
import code
for i in xrange(100000):
    code.randTest()
'''
'''
import code
maze = code.TEST_F
path = code.optimalPaths(code.calcPathMinDistancesFrom(maze, 0, 0, 19, 19))
code.printMatrixB(code.calcDistFromPathMatrix(maze, path), [-1])
'''
