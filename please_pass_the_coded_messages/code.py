# Convert list of ints to number, where position
# directly coorelates to digit place
def listToInt(l):
    value = 0
    for i in range(len(l)):
        place = len(l) - i - 1
        value += l[i] * pow(10, place)
    return value

# Given an array, compare all sublists to a condition.
# If the condition is met, return array of indices of
# sublist's elements in main list l.
# Precondition: tree = [len(l) - 1]
def allSublistsRec(l, tree, condition, k, r):
    if condition(l, tree, k, r):
        return tree
    else:
        # generate a new sublist index tree
        # [4] -> [3]
        # [3] -> [2]
        # [2] -> [1]
        # [1] -> [0]
        # [0] -> [4, 3]
        # [4, 3] -> [4, 2]
        # [4, 2] -> [4, 1]
        # [4, 1] -> [4, 0]
        # [4, 0] -> [4, 3, 2]
        while True:
            tree[-1] -= 1
            if len(tree) > len(l):
                return []
            elif tree[-1] < 0:
                tree[-1] = len(l) - len(tree)
                tree.append(len(l) - len(tree))
            else:
                break
        return allSublistsRec(l, tree, condition, k, r)

# Programmer-friendly wrapper for allSublistsRec method
def allSublists(l, condition, k, r):
    return allSublistsRec(l, [len(l) - 1], condition, k, r)

# Generate a sublist from a list and an index tree
def sublistFromTree(l, tree):
    sublist = []
    for i in range(len(tree) - 1, -1, -1):
        sublist.append(l[tree[i]])
    return sublist

# Given a list l and a sublist index tree named tree,
# return True if the sum if the sublist's elements
# is divisible by k
def sublistSumIsProduct(l, tree, k, r):
    sublist = sublistFromTree(l, tree)
    return (listToInt(sublist) % k == r)

def answer(l):
    # sort array biggest to smallest
    l = sorted(l, reverse=True)
    if len(l) == 0:
        return 0

    r = listToInt(l) % 3 # remainder from division
    if r == 0:
        return listToInt(l)

    # find the least-changing sublist divisible by r
    tree = allSublists(l, sublistSumIsProduct, 3, r)

    # remove all sublist elements from the list
    for i in tree:
        del l[i]

    if len(l) > 0:
        return listToInt(l)
    else:
        return 0
