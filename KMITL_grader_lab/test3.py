class TestClass:
    def __init__(self):
        self.size = 0

    def __len__(self):
        return self.size

    def plus(self):
        self.size += 1

    def minus(self):
        self.size -= 1


A = TestClass()

# don't use same name as function and variable
print(len(A))
A.plus()
A.plus()
print(len(A))
