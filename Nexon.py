def d(n):
    sum = n
    m = len(str(n))
    for i in range(m):
        digit = n%(10**(i+1))
        digit = digit/(10**i)
        sum += int(digit)
        
    return sum

sum1 = 0

for i in range(1, 5000):
    sum1 = sum1 + d(i)

print(sum1)
