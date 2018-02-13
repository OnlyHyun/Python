"""

0의 개수
1의 개수
2의 개수 뭐 이런 식?


"""

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, 1001):
    for j in range(0, 10):
        a[j] += str(i).count(str(j))


for i in range(10):
    print("%s:%s개" % (i, a[i]))



for x in range(10):
    print('%d: %d'%(x,''.join(map(str, range(1, 1001))).count(str(x))))

from collections import defaultdict

d = defaultdict(int)
for n in range(1, 1001):
    for x in str(n):
        d[x] += 1

print(d)


count={ x:0 for x in range(0,10) }

for x in range(1,101):
    for i in str(x):
        count[int(i)]+=1
        print(i)
        
print(count)
