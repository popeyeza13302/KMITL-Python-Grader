inputlst, inputpath = input('Enter : ').split('/')

'''
# *** !!! READ ME !!! **
    this is dijkstra shortestPath concept by sir.sirawit 
    
    1. make adjacency matrix 2D
        1.1 node 1D 
    2. created ...
        2.1 visited 1D       progress of dijkstra 
        2.2 weightlst 1D     progress of dijkstra 
        2.3 prevlst 1D       later..use for find shorest path in the end 
        
        2.4 weightlst[startindex] set to 0 *** ALWAYS ! (distance if self is 0)
        
    3. methods
        3.1 shortest dijkstra recursive (update all shortest distance from start to end)
        3.2 print shortest (from prevlst) track back to origin 
    4. DONE ! 
    
    caution : 
        - careful of can't find path...
            - minIndex = 999 (infinity)
            - (start or end) not in node 
'''
node = []

for i in inputlst.split(','):
    i = i.split()

    firstNode = i[0]
    endNode = i[2]

    if firstNode not in node:
        node.append(firstNode)
    if endNode not in node:
        node.append(endNode)

node.sort()
# print(node)

# build adjacency matrix 2D
matrix = [[0 for i in range(len(node))] for i in range(len(node))]

for i in inputlst.split(','):
    i = i.split()

    start = node.index(i[0])
    weight = int(i[1])
    end = node.index(i[2])

    matrix[start][end] = weight     # directional graph


# for i in matrix:
#    print(i)

def shortestPath(start, end, visited, weightlst, prevlst):
    startIndex = node.index(start)      # init start index
    visited.append(node[startIndex])    # add startNode to visit

    if start == end:    # base case
        return

    # begin with relaxation
    for index, col in enumerate(matrix[startIndex]):
        if col != 0:          # if row has some arrow(value)    # dijkstra formula
            if weightlst[startIndex] + col < weightlst[index]:  # allDistance[u] + distance[u-v] < distance[v] ->replace
                weightlst[index] = weightlst[startIndex] + col  # replace with low value
                prevlst[index] = start                        # add prevNode to lst (for track back to start in the end)
    # done with relaxation

    min = 999           # init min
    minIndex = 999      # init min index
    # for selected min with not already visited
    for index, col in enumerate(weightlst):
        if col < min and node[index] not in visited:
            min = col
            minIndex = index

    if minIndex == 999:  # can't go to destination (case of all are already visited and nothing change from 999)
        return
    else:
        shortestPath(node[minIndex], end, visited, weightlst, prevlst)      # recursive go next minNode


def printShortest(start, end, prevlst):
    stack = []
    currentNode = end
    currentIndex = node.index(currentNode)
    findPath = True
    if prevlst[currentIndex] == -1:     # can't go to start !
        findPath = False
    else:
        while currentNode != start:
            stack.append(currentNode)               # store currentNode now to stack
            currentIndex = node.index(currentNode)     # get currentIndex out of currentNode
            currentNode = prevlst[currentIndex]        # assign currentNode to prevNode
        else:
            stack.append(currentNode)              # store the last one

    # print statement result
    if len(stack) == 0 and findPath is False:
        print(f'Not have path : {startNode} to {endNode}')  # don't have node
    else:
        print(f'{startNode} to {endNode} : ', end='')   # from _ to _

        while len(stack) > 1:
            print(f'{stack.pop()}->', end='')       # print next
        else:
            print(f'{stack.pop()}', end='')         # last print

        print()


for i in inputpath.split(','):

    i = i.split()
    startNode = i[0]  # init start node
    endNode = i[1]  # init end node

    # check if startNode and endNode it exist ?
    if (startNode not in node) or (endNode not in node):
        print(f'Not have path : {startNode} to {endNode}')
        continue

    # initial new array //every inputpath
    visited = []
    weightlst = [999 for i in range(len(node))]  # infinity +++
    prevlst = [-1 for i in range(len(node))]

    # initial new value distance for first start
    weightlst[node.index(startNode)] = 0  # init new distance

    shortestPath(startNode, endNode, visited, weightlst, prevlst)
    printShortest(startNode, endNode, prevlst)

# v0 1 v1,v1 1 v2,v2 1 v3,v0 1 v3/v0 v1,v0 v2,v0 v3
# 1 2 2,1 4 3,2 1 3,2 7 4,3 3 5,4 1 6,5 2 4,5 5 6/1 6