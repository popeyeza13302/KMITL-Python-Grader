# week 5
class Queue:
    def __init__(self, lst=None):
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
        return self.tail()

    def front(self):  # Front
        return self.item[0]

    def tail(self):  # Tail
        return self.item[-1]

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)


def encodemsg(q1, q2):
    lst = []
    strQ = Queue(q1.item.copy())
    numQ = Queue(q2.item.copy())
    for _ in range(strQ.size()):
        if strQ.front() == ' ':
            strQ.deQ()
        else:
            char = ord(strQ.front())
            num = numQ.enQ(int(numQ.deQ()))
            if 65 <= char + num <= 90 and chr(char).isupper() or 97 <= char + num <= 122 and chr(char).islower():
                char = ord(strQ.deQ())
            else:
                char = ord(strQ.deQ()) - 26  # if y +2 -> a
            lst.append(chr(char + num))
    return lst

def decodemsg(q1, q2):
    encodeQ = Queue(encodemsg(q1, q2))
    numQ = Queue(q2.item.copy())
    lst = []
    for _ in range(encodeQ.size()):
        char = ord(encodeQ.front())
        num = numQ.enQ(int(numQ.deQ()))
        if 65 <= char - num <= 90 and chr(char).isupper() or 97 <= char - num <= 122 and chr(char).islower():
            char = ord(encodeQ.deQ())
        else:
            char = ord(encodeQ.deQ()) + 26   # if a -2 -> y
        lst.append(chr(char - num))
    return lst


q_str, q_num = map(Queue, map(list, input('Enter String and Code : ').split(',')))

print('Encode message is : ', encodemsg(q_str, q_num))
print('Decode message is : ', decodemsg(q_str, q_num))
