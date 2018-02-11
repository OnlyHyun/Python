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

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다" % treeHit)
    if(treeHit == 10):
        print("나무 넘어간드아아아")


prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

"""

number = 0
while number != 4:
    print(prompt)
    number = int(input("Enter Number:"))

a = 1
if a: pass
else: print(a)

a = 0
if a: pass
else: print(a)


coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

sum = 0
for i in range(1, 11):
    sum += i

print(sum)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print(' ')
    
