"""
Spiral Array

나선형 배열

가정

방법은 두 가지가 있을 것이다
1. 실제로 나선형 배열의 규칙성을 찾아내서 반복문을 통해
나선형배열이 실제 도는 방향대로 차례대로 값을 입력하는 방식

2. 배열이 도는 순서대로 값을 입력하는 것이 아니라 규칙성을 찾아내
반복문에 계산을 통해 바로바로 그냥 값을 바로바로 넣어주는 방식

이 있을 것이라고 생각된다

먼저 최대한 1번의 방식으로 접근하고자 한다

번갈아가면서 증가, 감소를 보이며
세로 움직일 땐 가로 고정, 가로 움직일 땐 세로 고정

"""

S = list(map(int, str(input("입력하라: ")).split()))

Spiral = [[0]*S[1] for i in range(S[0])]

Max = S[0]*S[1]-1

N = S[0]-1
M = S[1]-1


Count = M+1
Sign = 1
n = M
m = 0

for i in range(M+1):
    Spiral[0][i] = i


while True:
    
    for i in range(N):
        m += Sign
        Spiral[m][n] = Count
        Count += 1
        
        
    N -= 1
    Sign *= -1
    
    for i in range(M):
        n += Sign
        Spiral[m][n] = Count
        Count += 1

    M -= 1

    if(Count > Max): break

for i in range(S[0]):
    print(Spiral[i])
    
