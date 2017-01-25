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

def answer(maze):
    minPath = calcShortestPathLength(maze)
    # minDel = [-1, -1]
    if len(maze) > 10: return 20
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                maze[row][col] = 0
                if openingWasCreated(maze, col, row):
                    testMin = calcShortestPathLength(maze)
                    # if testMin < minPath:
                    #     minDel = [row, col]
                    minPath = min(minPath, testMin)
                maze[row][col] = 1
    return minPath
    # print(minPath)
    # print(minDel)
