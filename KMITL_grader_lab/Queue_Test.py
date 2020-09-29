class Queue:
    def __init__(self,lst = None):
        if lst == None:
            self.item = []
        else:
            self.item = lst

    def __str__(self):
        s = ''
        for i in self.item:
            s += str(i)
        return s

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def enQueueRight(self, data):
        self.item.append(data)

    def enQueueLeft(self, data):
        self.item.insert(0, data)

    def deQueueLeft(self):
        return self.item.pop(0)

    def deQueueRight(self):
        return self.item.pop()

x = [1,2,3,4,5,6,7,8]
Q = Queue()

for i in x:
    Q.enQueueLeft(i)

print(Q)

for i in range(Q.size()):
    print(Q.deQueueLeft())

