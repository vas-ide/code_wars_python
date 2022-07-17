def each_cons(lst, n):
    # your solution here
    result = []
    sigment = []
    for i, value in enumerate(lst):
        if n == 1:
            result.append([value])
        if len(sigment) < n:
            sigment.append(value)
        if len(sigment) == n:
            result.append(sigment)
            sigment = [lst[i - 1], value]
    print(result)




lst = [3, 5, 8, 13]
each_cons(lst, 3)

