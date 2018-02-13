sum1 = 0
sum = [0 for i in range(1001)]

for i in range(10, 1001):
    sum[i] = 1
    for j in str(i):
        if(j == int(0)):
            sum[i] = 0
            break
        else:
            sum[i] *= int(j)
    sum1 += sum[i]

print(sum1)

"""

print(sum(eval('*'.join(str(x))) for x in range(10,1001)))

내포문으로는 어떻게 맞춰서 변형시킬 지 모르겠음

"""
y = 0

for x in range(10, 1001):
    y += eval('*'.join(str(x)))
print(y)
