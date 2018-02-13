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
