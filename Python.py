a = [1, 2, 3, 4]
while a:
    print(a.pop())
print(type(3))

a = 3
b = 3
print(a is b)

import sys
print(sys.getrefcount(3))

a, b = ('python', 'life' )
print(a,"\n",b)

[a, b] = ['python', 'life']
print(a, b)

a = b = 'Python'
print(a, b)

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)

b = a[:]
a[1] = 2
print(a,"\n",b)

from copy import copy
b = copy(a)

print(a is b)
