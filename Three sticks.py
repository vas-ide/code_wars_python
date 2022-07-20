def maxlen(L1,L2):
    # return maximal length
    max_stick = L1
    min_stick = L2
    if L1 < L2:
        max_stick = L2
        min_stick = L1
    else:
        max_stick = L1
        min_stick = L2

    if max_stick / min_stick >= 2 and min_stick >= max_stick / 3:
        print(min_stick)
        return min_stick
    elif min_stick > max_stick / 2:
        print(max_stick / 2)
        return max_stick / 2
    else:
        print(max_stick/3)
        return max_stick / 3

maxlen(12,5)
maxlen(5,12)
maxlen(61,120)

