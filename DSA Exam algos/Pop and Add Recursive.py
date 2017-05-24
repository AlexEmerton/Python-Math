A = [2, 3, 5, 6, 8]
B = []


def p_add(ST):
    i = 0
    sum = 0

    if IsEmpty(ST):
        return 0
    else:
        x = ST[0]
        sum += ST.pop(i)
        ST.append(x)

        while ST[0] != x:
            y = ST.pop(i)
            sum += y
            ST.append(y)

    return sum


def IsEmpty(array):
    if len(array) == 0:
        return True
    else:
        return False

print(p_add(A))
