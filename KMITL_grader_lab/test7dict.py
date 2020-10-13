sett = {1,1,2}
print(type(sett))
print(sett)

print(dir(dict))
A = dict(one=1,two=2,three=3)
B = {'one':1, 'two':2, 'three':3}

print(A)
print(B)
print(type(A))
print(type(B))

print(A['one'])
print(A['two'])

print(A.get('new', 0))
print(A)


for i in (B.values()):
    B[i] = B.get(i,0)+1

print(B)