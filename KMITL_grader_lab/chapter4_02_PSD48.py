class Queue:
    def __init__(self):
        self.itemN = []
        self.itemS = []
        self.item = []

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        return 'Number in Queue is :  ' + str(self.bigItem())

    def deQ(self):

        if self.isEmpty():
            return 'Empty'
        elif not len(self.itemS) == 0:
            return self.itemS.pop(0)
        elif not len(self.itemN) == 0:
            return self.itemN.pop(0)

    def enQ(self, i, mode=False):
        if not mode:
            self.itemN.append(i)
        else:
            self.itemS.append(i)

    def isEmpty(self):
        return len(self.bigItem()) == 0

    def size(self):
        return len(self.bigItem())

    def bigItem(self):
        self.item.clear()
        self.item.extend(self.itemS)
        self.item.extend(self.itemN)
        return self.item


lst = [str(i) for i in input('Enter Input : ').split(',')]

q = Queue()

for i in lst:
    i = i.split()
    if i[0] == 'EN':
        q.enQ(i[1])
    elif i[0] == 'ES':
        q.enQ(i[1], True)
    elif i[0] == 'D':
        print(q.deQ())
