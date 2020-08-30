class Stack:
    """< Default Stack >"""
    def __init__(self, list=None):
        self.value = 0
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of ' + str(self.size()) + ' items : '
        for i in self.items:
            s += str(i) + ' '
        return s

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class StackCalc():
    def __init__(self):
        self.value = 0

    def run(self, lst):
        lst = lst.split()
        stack = Stack()
        for i in lst:

            if i == 'DUP':
                stack.push(stack.peek())
                continue
            if i == 'POP':
                stack.pop()
                continue
            if i == 'PSH':
                continue

            if i in '+-*/':
                a, b = stack.pop(), stack.pop()
                if i == '+':
                    stack.push(a+b)
                elif i == '-':
                    stack.push(a-b)
                elif i == '*':
                    stack.push(a*b)
                elif i == '/':
                    stack.push(a/b)
            else:
                try:
                    stack.push(int(i))
                except:
                    print('Invalid instruction:', i)
                    quit()
        else:
            if not stack.isEmpty():
                self.value = stack.pop()

    def getValue(self):
        return round(self.value)


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
