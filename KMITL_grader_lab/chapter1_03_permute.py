# week 1
def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


print('*** Fun with permute ***')
num = [int(i) for i in input('input : ').split(',')]

print('Original Cofllection: ', num)
print('Collection of distinct numbers:')
num.reverse()
case = 0
if len(num) == 3:
    case = 1
elif len(num) == 4:
    case = 2
# print('length = ', len(num))
# print('reverse = ', num)
totalList = []
starterList = []
# append to new List
for i in range(len(num)):
    starterList.append(num[i])

start = 0
next = 0
if case == 1:
    # append to totalList
    totalList.append(starterList)
    for i in range(factorial(len(num))-1):
        # print('--------------')
        #print('loop =', i)
        newList = []

        start = -len(num)+i
        next = -len(num)+1+i
        #print('start = ', start)
        #print('next = ', next)

        # swap!!!
        num[start], num[next] = num[next], num[start]

        # append to new List
        for i in range(len(num)):
            newList.append(num[i])

        # append to totalList
        totalList.append(newList)

        # print('totalList now = ', totalList)
        #print('--------------')
elif case == 2:

    case2List = []
    for i in range(1, len(num)):
        case2List.append(num[i])
    for i in range(factorial(len(num))):


        if i%4 == 0:
            caseList = []
            caseList.append(starterList[0])
            i = i//4
            newList = []
            start2 = -len(num) + i
            next2 = -len(num) + 1 + i
            # swap!!!
            if i != 0:
                case2List[start2], case2List[next2] = case2List[next2], case2List[start2]
            # append to new List
            for i in range(len(num)):
                newList.append(num[i])
            # extend to caseList
            caseList.extend(case2List)
            # append to totalList
            totalList.append(caseList)
        else:
            if i%4 == 1:
                num = caseList.copy()
            i = (i % 4)-1
            newList = []
            start = -len(num) + i
            next = -len(num) + 1 + i

            # swap!!!
            num[start], num[next] = num[next], num[start]
            # append to new List
            for i in range(len(num)):
                newList.append(num[i])

            # append to totalList
            totalList.append(newList)

print('', totalList)
