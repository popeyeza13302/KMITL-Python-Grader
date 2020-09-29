x = 1
y = 257
print(id(x))
print(id(y))
x += 2
y = x
print(id(x))
print(id(y))

s = 'outside'

def testfx():
    global s
    print(s)
    s = 'inside'
    print(s)

print(s)
testfx()

print(s)

def max(x,y):
    if x > y :
        print('X =', x)
    else:
        print('Y =',y)

max('heasddas','t')
print(s.upper())
s = s.upper()
print(s)
print(s.capitalize())
s.replace('IN','out',1)
print(s)
lst = [3,2,1]
lst.insert(-123123123,0)
lst.insert(999,1)
lst.insert(5,7)
print(lst)

#caution! pop out of bound
#caution! remove x not in list
lst.sort()
print(lst)
sorted(lst)
reversed(lst)    # ???
print(lst)


tp = tuple([1,2,3,4,5])
print(tp.index(4))


print(chr(65))
print(ord('A'))

for i,j in zip(range(5),range(5)):
    print(i)
    print(j)