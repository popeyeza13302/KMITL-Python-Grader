# week 5
class Queue:
    def __init__(self, que):
        self.item = []  # for id
        self.num = []   # for depart num
        self.department = que   # dict()

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        return 'Number in Queue is :  ' + str(self.item)

    def deQ(self):
        if self.isEmpty():          # empty
            return 'Empty'
        self.num.pop(0)             # pop number out
        return self.item.pop(0)     # pop id out

    def enQ(self, i):
        myValue = 0
        for key, value in self.department.items():
            if key == i:                # find depart num by id
                myValue = value             # get depart num

        if self.isEmpty():              # first time
            self.item.append(i)             # add to id
            self.num.append(myValue)        # add to depart num
        else:
            have = False  # have same depart or not?
            for j in range(self.size() - 1, -1, -1):    # check from last to first
                if self.num[j] == myValue:                  # same num ?
                    self.item.insert(j + 1, i)                  # insert id to next one
                    self.num.insert(j + 1, myValue)             # insert num to next one
                    have = True                                 # have same depart in row !
                    break
            if have is False:           # if you don't have same depart in row
                self.item.append(i)         # add id to last
                self.num.append(myValue)    # add num to last

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)


lst, seq = input('Enter Input : ').split('/')

department = dict()

for i in lst.split(','):
    i = i.split()
    department[int(i[1])] = int(i[0])  # assign to dict()

mainQ = Queue(department)

for i in seq.split(','):
    i = i.split()
    if i[0] == 'E':
        mainQ.enQ(int(i[1]))
    elif i[0] == 'D':
        print(mainQ.deQ())
