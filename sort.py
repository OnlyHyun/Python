"""

1, 2, 3, 4, 5

자기보다 크면 카운팅
자기보다 작은 친구 만나면 스탑
0
0 break
1
1 break 0
2
2 break 1 0
0
3 2 1 0 break

자기가 들어가야 할 위치 파악

"""
"""
풀이 1)
"""

n = list(map(int, str(input("배열을 입력하라: ")).split()))

for i in range(1, len(n)):
    c = 0
    for j in range(i-1, -1, -1):
        if(n[i] < n[j]): c += 1
        else: break
    n.insert(i-c, n[i])
    del n[i+1]
    print(n)    

"""
풀이 2)

n = list(map(int, str(input("배열을 입력하라: ")).split()))

for i in range(1, len(n)):
    c = 0
    for j in range(i-1, -1, -1):
        if(n[i] < n[j]): c += 1
        else: break

    k = n[i]
    for j in range(i-1, i-c-1, -1):
        n[j+1] = n[j]
            
    n[i-c] = k
    print(n)
"""
