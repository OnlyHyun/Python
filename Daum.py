s = [1, 3, 4, 8, 13, 17, 20]

s = sorted(s)

min = max(s)

i=0

while True:
    length = int(s[i+1]) - int(s[i])
    if(min > length):
        min_length = [s[i], s[i+1]]
        min = length
    i+=1
    if(len(s) == i+1): break

print(min_length)

    
"""
for i in range(len(s)):
    for j in range(i+1, len(s)):
        length = abs(s[i] - s[j])
        if(min > length):
            min_length = [s[i], s[j]]
            min = length

print(min_length)            

"""


"""

s= [1, 3, 4, 8, 13, 17, 20]
pairs = list(zip(s[0:], s[1:]))
print(pairs)
pairs.sort(key = lambda x:x[1]-x[0])
print(pairs[0])

"""
