import math


def dec_inc(arr):
    flag = True
    d = 0
    t = len(arr) - 1
    for x in range(0, len(arr)-1):
        if arr[x] < arr[x+1]:
            flag = False
            return flag
    if flag:
        if len(arr) % 2 == 0:
            while d != (len(arr)/2):
                temp = arr[d]
                arr[d] = arr[t]
                arr[t] = temp
                d += 1
                t -= 1
        else:
            while d != math.floor((len(arr)/2)):
                temp = arr[d]
                arr[d] = arr[t]
                arr[t] = temp
                d += 1
                t -= 1
    return arr

A = [6, 5, 4, 3, 2, 1]
B = [5, 4, 3, 2, 1]
C = [1, 2, 1]
print(dec_inc(A))
print(dec_inc(B))
print(dec_inc(B))


