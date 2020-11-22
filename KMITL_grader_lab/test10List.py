vertex = ['1', '2', '3', '4', '5']

edge_lst = ['0 1', '0 2', '1 0', '1 3', '2 0']



adj_lst = [[] for i in range(len(vertex))]


for e in edge_lst:
    v, v_next = [int(i) for i in e.split()]

    adj_lst[v].append(v_next)


print(adj_lst)


answer = [[1,2],[2,3],[4,2],[2,11]]

for i in enumerate(answer):
    print(i)