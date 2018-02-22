"""
S = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5']
S1 = [ 0 for i in range(0, len(S)) ]
S2 = []
count = 0

while True:

    S1[count] = 0
    
    if(S[0][0] == S[1][0]):
        S1[count] = S.pop(0)
        count+=1
    else:
        S1[count] = S.pop(0)
        break
    
del S1[count+1:]

for i in range(0, count+1):
    S2.append(S1[i])
    S2.append(S[i])

print(S2)
"""

S = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5']
S1 = []

n = int(len(S)/2)

for i in range(0, n):
    S1.append(S[i])
    S1.append(S[n+i])

print(S1)
