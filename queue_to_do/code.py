def answer(start, length):

    # initialize variables
    startIsEven = (start % 2 == 0)
    lengthIsEven = (length % 2 == 0)

    # calculate result for various cases (not using brute-force)
    if not startIsEven and not lengthIsEven: # start = odd, length = odd
        result = 0
        for i in range(start, start + length * length, length * 2):
            result ^= i
        return result
    elif startIsEven and not lengthIsEven: # start = even, length = odd
        result = 0 if (length - 1) % 4 == 0 else 1
        for i in range(start + length, start + length * length, length * 2):
            row = int((i - start) / length)
            result ^= i
            result ^= i + length - row - 1
            result ^= i - row
        result ^= start + length * (length - 1)
        return result
    elif not startIsEven and lengthIsEven: # start = odd, length = even
        result = 0
        for i in range(start, start + length * length, length * 2):
            row = int((i - start) / length)
            result ^= i
            result ^= i + length
            result ^= i + length - row - 1
        return result
    else: # start = even, length = even
        result = 0 if length % 4 == 0 else 1
        for i in range(1, length + 1, 2):
            result ^= start + length * (i + 1) - i - 1
        return result
