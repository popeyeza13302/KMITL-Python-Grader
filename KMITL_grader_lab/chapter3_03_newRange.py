print('*** New Range ***')
listInput = [float(i) for i in input('Enter Input : ').split()]


def oneFunction(ls):
    listOutput = []
    start = 0.0
    stop = 0.0
    step = 1.0

    if len(listInput) == 1:
        stop = ls[0]
    elif len(listInput) == 2:
        start, stop = ls[0], ls[1],
    elif len(listInput) == 3:
        start, stop, step = ls[0], ls[1], ls[2]
    else:
        return 'Error'

    while start < stop:
        listOutput.append(round(start, 3))
        start += step

    return tuple(listOutput)


print(oneFunction(listInput))
