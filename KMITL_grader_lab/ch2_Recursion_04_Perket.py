def perket(lst, binary, index):
    if index == len(binary):
        return 1, 0

    sourSum, bitterSum = perket(lst, binary, index + 1)

    if binary[index] == '1':
        s, b = map(int, lst[index].split())
        sourSum *= s
        bitterSum += b

    return sourSum, bitterSum


theMin = -99
inp = input('Enter Input : ').split(',')

for i in range(1, 2 ** len(inp)):
    sour, bitter = perket(inp, bin(i).replace('0b', '').zfill(len(inp)), 0)
    total = abs(sour - bitter)
    if i == 1:
        theMin = total
    else:
        if abs(sour - bitter) < theMin:
            theMin = total

print(theMin)
