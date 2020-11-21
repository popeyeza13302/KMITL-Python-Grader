inputlst = input('Enter : ').split(',')

node = []
for i in inputlst:
    i = i.split()
    for k in range(2):
        if i[k] not in node:
            node.append(i[k])

node.sort()
#print(node)

matrix = [[0 for i in range(len(node))] for i in range(len(node))]

# using adjacency matrix to stored the data (I think it easy to coding)

for i in inputlst:
    i = i.split()
    start = node.index(i[0])
    end = node.index(i[1])

    matrix[start][end] = 1      # undirected graph used to be like this (no arrow) (both way)
    matrix[end][start] = 1

#for row in matrix:
#    print(row)


# function depth first Traversals
visited = []
def depthFirst(row):    # recursive

    print(node[row], '', end='')    # print current visited
    visited.append(node[row])       # add node to visited

    for index, col in enumerate(matrix[row]):   # every row in matrix
        if col == 1 and node[index] not in visited:  # find 1 with not in visited
            depthFirst(index)       # go on to next row


# function bredth first Traversals
def bredthFirst():

    for row in range(len(node)):                        # every row
        if node[row] not in visited:        # init first node if don't in visited yet...
            visited.append(node[row])
            print(node[row], '', end='')

        for index, col in enumerate(matrix[row]):       # every column
            if col == 1 and node[index] not in visited:     # find 1 with not in visited
                visited.append(node[index])
                print(node[index], '', end='')



# A B,B C,A D
print('Depth First Traversals : ', end='')
for i in range(len(node)):
    if node[i] not in visited:
        depthFirst(i)

print()
visited.clear()
print('Bredth First Traversals : ', end='')
bredthFirst()