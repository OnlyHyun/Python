def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(GuGu(2))

""" 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라 """

sum = 0
for i in range(1, 1000):
    if(i % 3 == 0 or i % 5 == 0):
        sum += i

print(sum)

import math

def getTotalPage(m, n):
    page = math.ceil(m/n)
    return page

print((getTotalPage(5, 10)))
print((getTotalPage(15, 10)))
print((getTotalPage(25, 10)))
print((getTotalPage(30, 10)))

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt', 'r')
    print(f.readlines())
    f.close()
    
