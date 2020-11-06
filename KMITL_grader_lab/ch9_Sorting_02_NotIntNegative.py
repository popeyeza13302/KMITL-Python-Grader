lst = [int(i) for i in input('Enter Input : ').split()]

# selection sort (lock max)
for loop in range(1, len(lst)):  # amount of number in list
    maxIndex = 0

    # find max index
    for i in range(len(lst)+1-loop):
        # special case
        if lst[i] < 0:
            continue
        elif lst[i] > lst[maxIndex]:
            maxIndex = i

    # special case
    if lst[len(lst)-loop] < 0:
        continue
    else:
        # swap max and last index
        lst[len(lst)-loop], lst[maxIndex] = lst[maxIndex], lst[len(lst)-loop]

for i in lst:
    print(i, end=' ')

