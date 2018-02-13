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
