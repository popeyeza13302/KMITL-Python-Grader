powerList, groupList = input('Enter Input : ').split('/')

powerList = [int(i) for i in powerList.split()]
groupList = [str(i) for i in groupList.split(',')]

sumList = []


def recursionTree(n):
    sum = 0                             # initial sum = 0

    if n >= len(powerList):             # if out of array
        return 0

    sum += recursionTree(2 * n + 1)     # go index left
    sum += recursionTree(2 * n + 2)     # go index right
    return powerList[n] + sum           # sum of (powerList[index] + sum)


print(recursionTree(0))                 # node sum (index = 0)

for i in groupList:
    i = list(map(int, i.split()))       # 2 group compare
    sum1 = recursionTree(i[0])          # group 1st
    sum2 = recursionTree(i[1])          # group 2nd

    if sum1 > sum2:
        print(i[0], '>', i[1], sep='')
    elif sum1 < sum2:
        print(i[0], '<', i[1], sep='')
    else:
        print(i[0], '=', i[1], sep='')
