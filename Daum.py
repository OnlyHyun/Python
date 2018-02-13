s = [1, 3, 4, 8, 13, 17, 20]

print(min(s))

min_length = max(s) - min(s)
min = max(s)

for i in range(len(s)):
    for j in range(i+1, len(s)):
        length = abs(s[i] - s[j])
        if(min > length):
            min_length = [s[i], s[j]]
            min = length

print(min_length)            


"""

s= [1, 3, 4, 8, 13, 17, 20]
pairs = list(zip(s[0:], s[1:]))
print(pairs)
pairs.sort(key = lambda x:x[1]-x[0])
print(pairs[0])

"""
