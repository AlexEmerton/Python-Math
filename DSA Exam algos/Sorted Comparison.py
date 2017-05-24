def sorted_check(arr1, arr2):
    C = []
    flag = 0

    k = 0
    p = 0

    while p < len(arr1) and k < len(arr2):
        if arr1[p] == arr2[k]:
            flag = k + 1
            break
        elif arr1[p] < arr2[k]:
            p += 1
        else:
            C.append(arr2[k])
            k += 1

    if flag > 0:
        C += arr2[flag:]
    # print(C)
    return C

A = [6, 10, 15, 25, 100]
B = [2, 4, 7, 11]
print(sorted_check(A, B))

