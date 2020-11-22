inputlst, inputpath = input('Enter Input : ').split('/')
inputpath = inputpath.split()

node = []
for i in inputlst.split(','):
    i = i.split()
    for k in range(2):
        if i[k] not in node:
            node.append(i[k])

node.sort()
#print(node)

matrix = [[0 for i in range(len(node))] for i in range(len(node))]

for i in inputlst.split(','):
    i = i.split()
    startIndex = node.index(i[0])
    endIndex = node.index(i[1])

    matrix[startIndex][endIndex] = 1
    matrix[endIndex][startIndex] = 1

#for i in matrix:
#    print(i)

start = inputpath[0]
end = inputpath[1]

# 1 2,3 4,3 2,4 5,5 1,3 5/1 3

visited = []
answer = []

def findpath(start, end, visited):  # recursive

    visited.append(start)   # add start to visited
    row = node.index(start)     # get row index of start

    if start == end:    # base case
        for index, lst in enumerate(answer):    # sorted lst of length
            if len(visited) < len(lst):             # if len visited (less than) len answer
                answer.insert(index, visited)           # insert between lst in answer
                break                                   # break out
        else:
            answer.append(visited)              # if not found...append last one
        return

    for index, col in enumerate(matrix[row]):
        if col == 1 and node[index] not in visited:     # col==1 and not yet visited ...  go to visited
            findpath(node[index], end, visited.copy())  # recursive


findpath(start, end, visited)
if len(answer) > 0:                            # have possible way > 0
    print(f'All possible path from {start} to {end} :')
    for lst in answer:
        print(' -> '.join(lst))
else:
    print(f'{start} can\'t go to {end}')        # no way (0 way)


