def each_cons(lst, n):
    # your solution here
    lst_upd = []
    for j in lst:
        if type(j) == list:
            for y in j:
                lst_upd.append(y)
        else:
            lst_upd.append(j)
    print(lst_upd)

    result = []
    sigment = []
    for i, value in enumerate(lst_upd):
        if n == 1:
            result.append(value)
        if len(sigment) < n:
            sigment.append(value)
        if len(sigment) == n:
            result.append(sigment)
            sigment = [lst_upd[i - 1], value]
    print(result)
    return result




lst = [3, 5, 8, 13]
each_cons(lst, 2)
lst = [[20], [20], [13], [7], [8]]
each_cons(lst, 2)
lst = [[2], [3], 4, 5, 6]
each_cons(lst, 3)
