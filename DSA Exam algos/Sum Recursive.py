A = [1, 10, 10]


def el_sum(ST, sum):
    if IsEmpty(ST):
        return sum
    else:
        sum += ST.pop(len(ST)-1)
        print('added an item. sum = ', sum)
        return el_sum(ST, sum)


def IsEmpty(array):
    if len(array) == 0:
        return True
    else:
        return False

print(el_sum(A, 0))

