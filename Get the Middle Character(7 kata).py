def get_middle(s):
    #your code here
    if len(s) <= 2:
        #print(s)
        return s
    else:
        new_string = ' '
        counter = 0
        while counter < len(s) // 2:
            counter += 1
            new_string += s[counter]
        #print(new_string)
        if len(s) % 2 == 0:
            print(new_string[-2:])
            return new_string[-2:]
        else:
            print(new_string[-1])
            return new_string[-1]


get_middle("te")
get_middle("tes")
get_middle("test")
get_middle("testing")
get_middle("testqwertytest")

