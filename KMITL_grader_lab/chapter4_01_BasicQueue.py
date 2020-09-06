# week 5
class Queue:
    def __init__(self, lst = None):
        if lst == None:
            self.item = []
        else:
            self.item = lst

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        return 'Number in Queue is :  ' + str(self.item)

    def deQ(self):
        if self.isEmpty():
            return print(-1)
        return print('Pop', self.item.pop(0), 'size in queue is', self.size())

    def enQ(self, i):
        self.item.append(i)
        return self.item[-1]

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)


lst = [str(i) for i in input("Enter Input : ").split(',')]

q = Queue()

for i in lst:
    i = i.split()
    if i[0] == 'E':
        print('Add', q.enQ(i[1]), 'index is', q.size()-1)
    elif i[0] == 'D':
        q.deQ()

print(q)