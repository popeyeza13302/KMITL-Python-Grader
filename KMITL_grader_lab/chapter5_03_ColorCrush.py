class Stack:
    """< Default Stack >"""

    def __init__(self, list=None):
        self.string = ''
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        return self.string.join(self.items)

    def copy(self, other):
        self.items = other.items.copy()
        self.items.reverse()

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return self.items.clear()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


inp = input('Enter Input : ').split()

stk_inp = Stack(inp)
stk_cal = Stack()
stk_score = Stack()

combo = 0
ready = False

while True:
    firstSize = stk_inp.size()
    for i in range(stk_inp.size()):
        if i == 0:  # FIRST PUSH
            stk_cal.push(stk_inp.pop())
        else:
            if not stk_cal.isEmpty() and not stk_inp.isEmpty():  # CHECK IF NOT EMPTY
                if stk_cal.peek() != stk_inp.peek():    # CHECK IF SAME OR NOT
                    if not ready:
                        stk_cal.push(stk_inp.pop())     # FIRST ONE INTO CAL
                    else:
                        stk_cal.push(stk_score.pop())   # PUSH SCORE "BACK" TO CAL
                        stk_cal.push(stk_inp.pop())     # PUSH INP TO CAL
                        ready = False                   # SET READY = FALSE
                else:
                    if not ready:                       # SECOND ONE
                        stk_score.push(stk_inp.pop())   # PUSH INP TO SCORE
                        ready = True
                    else:
                        stk_cal.pop()                   # SCORE 3 STRIKE
                        stk_inp.pop()
                        stk_score.pop()
                        combo += 1
                        ready = False
    else:
        if firstSize == stk_cal.size():         # LAST
            print(stk_cal.size())
            if stk_cal.isEmpty():
                print('Empty')
            else:
                print(stk_cal)
            if combo > 1:
                print('Combo :', combo, '! ! !')
            break

        stk_inp.copy(stk_cal)   # EVERY LOOP HAS TO DO
        stk_cal.empty()         # EMPTY CAL


