def next_item(xs, item):
    xs_upd = []
    for i in xs:
        xs_upd.append(i)
    print(xs_upd)

    for i, value in enumerate(xs_upd):
        if value == item:
            print(xs_upd[i + 1])
            return xs_upd[i + 1]
        elif item not in xs_upd:
            print(None)
            return None
        elif item == xs_upd[-1]:
            print(None)
            return None

next_item([1, 2, 3, 4, 5, 6, 7, 8], 8)
next_item([1, 2, 3, 4, 5, 6, 7, 8], 6)
next_item(iter(range(1, 300)), 154)
next_item('testing', 't')