n = int(input("자연수 n 값을 입력하시오: "))

for i in range(1, n+1):
    print("O"* (n-i) + "X" * i)
  

"""

print((lambda n: '\n'.join('O'*(n-i) + 'X'*i for i in range(1,n+1)))(int(input('>>>'))))
한 줄로 풀기!

"""
