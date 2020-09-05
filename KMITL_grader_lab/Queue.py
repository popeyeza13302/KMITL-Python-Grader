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
        return self.item.pop(0)

    def enQ(self, i):
        self.item.append(i)
        return self.item[-1]

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)
