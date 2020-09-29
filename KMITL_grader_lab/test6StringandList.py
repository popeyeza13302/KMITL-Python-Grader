print(dir(str))
print(dir(list))

string = 'abcdefg'
print(string[::-1])  # reverse
print(string[-7:7])

numstr = 'aaaBBB'

# reverse string
# print(numstr[::-1])

print(numstr[0])
print(numstr.index('a'))
print(len(numstr))
print(numstr.capitalize())
print(numstr.upper())
print(numstr.lower())
print('#'.join(numstr))
print(numstr.replace('a', 'c'))

for i in numstr:
    print('forforfor',i)


lst = [1, 3, 5, 2, 4,4, 6]
print(len(lst))

lst.remove(4)
lst.remove(4)
print(lst)
lst.pop()
lst.pop()
lst.pop()
lst.pop()
lst.pop()
print('last',lst)



# reverse / reversed

# lst.reverse()
# print(lst) # right one

# print(lst[::-1]) # right one

# lst = reversed(lst)
# print(lst)   # wrong


# sort / sorted

# lst = sorted(lst)
# print(lst)  # right one

# print(sorted(lst))   right one

# lst.sort()
# print(lst) # right one

# print(lst.sort()) # wrong
