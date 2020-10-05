def fibRecursive(n):
    if n <= 1:
        return n
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)


for i in range(100):
    print(fibRecursive(i))