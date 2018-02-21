
n = int(input("정수 n을 입력하라: "))

count = 2
s = [0, 1]

while True:

    if(s[count-1] + s[count-2] > n): break

    s.append(s[count-1] + s[count-2])
    count += 1

print(s)
    
"""

n = int(input("정수 n을 입력하라: "))
a, b = 0, 1
print('0', end = ' ')
while b <= n:
    print(', %d' % b, end='')
    a, b = b, a+b
"""
