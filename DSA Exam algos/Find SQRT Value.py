import math


def f_squared(arr):
    C = []
    flag = False
    for i in range(0, len(arr)):
        C.append(math.sqrt(arr[i]))
    print(C)
    k = 0
    p = 0

    while p < len(C) and k < len(arr):
        if C[p] == arr[k]:
            flag = True
            break
        elif C[p] < arr[k]:
            p += 1
        else:
            k += 1

    return flag


A = [5, 10, 15, 25, 100]
print(f_squared(A))