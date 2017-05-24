# Not finished
# Need to initialise l_list structure in Python prior to testing and
# further construction


def link_ins(l_list, x):
    CurEl = l_list[0]
    found = False
    i = 0
    while not found:
        if CurEl == x or CurEl > x:
            found = True
        elif CurEl < x and i == len(l_list)-1:
            i = len(l_list)
        else:
            i += 1
            CurEl = l_list[i]

    return i


A = [1, 3, 5, 7]

print(link_ins(A, 9))

