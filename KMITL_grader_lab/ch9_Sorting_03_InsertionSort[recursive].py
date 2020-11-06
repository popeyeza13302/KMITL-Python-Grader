def insertionRecursion(array, n):
    # base case
    if n <= 1:
        return
    insertionRecursion(array, n-1)  # for bigger to small...

    last = array[n-1]   # store last value
    j = n - 2   # store before last index

    j = forLoopRecursion(array, j, last)     # for loop recursive

    array[j+1] = last   # assign last to the right position

    if len(array) != n:
        print(f'insert {last} at index {j+1} :', array[:n], array[n:])
    else:
        print(f'insert {last} at index {j+1} :', array)


def forLoopRecursion(array, j, last):
    # base case
    if j < 0 or array[j] < last:   # out of range and left is less than right
        return j

    array[j+1] = array[j]   # shift left position to right
    return forLoopRecursion(array, j-1, last)   # go left


lst = [int(i) for i in input('Enter Input : ').split()]

insertionRecursion(lst, len(lst))

print('sorted')
print(lst)