def recAnswer(start, length, lineCount):
    if lineCount == length:
        return 0
    xors = 0
    for i in range(start, start + length - lineCount):
        xors ^= i
    return xors ^ recAnswer(start + length, length, lineCount + 1)

def answer(start, length):
    # return recAnswer(start, length, 0)
    result = 0
    for i in range(length):
        for j in range(start + length * i, start + length * (i + 1) - i):
            result ^= j
    return result

def analyze(a, b):
    a1 = answer(a, b)
    a2 = answer(b, a)

    print('-----------------------')
    print('| start=' + str(a) + ': %2=' + str(a % 2) + ', %4=' + str(a % 4) + ' |')
    print('| length=' + str(b) + ': %2=' + str(b % 2) + ', %4=' + str(b % 4) + ' |')
    print('| result=' + str(a1) + ': %2=' + str(a1 % 2) + ', %4=' + str(a1 % 4) + ' |')
    size = round(b * (b + 1) / 2)
    print('| size=' + str(size) + ': %2=' + str(size % 2) + ', %4=' + str(size % 4) + ' |')
    print('-----------------------')
    p = (a % 2) ^ (b % 2) ^ (size % 2)
    print('Predict: result % 2 = ' + str(p))
    print('-----------------------')
    print('| start=' + str(b) + ': %2=' + str(b % 2) + ', %4=' + str(b % 4) + ' |')
    print('| length=' + str(a) + ': %2=' + str(a % 2) + ', %4=' + str(a % 4) + ' |')
    print('| result=' + str(a2) + ': %2=' + str(a2 % 2) + ', %4=' + str(a2 % 4) + ' |')
    size = round(a * (a + 1) / 2)
    print('| size=' + str(size) + ': %2=' + str(size % 2) + ', %4=' + str(size % 4) + ' |')
    print('-----------------------')
    p = (a % 2) ^ (b % 2) ^ (size % 2) FALSE
    print('Predict: result % 2 = ' + str(p))
