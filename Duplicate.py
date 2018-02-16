"""
0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

sample inputs: 0123456789 01234 01234567890 6789012345 012322456789

sample outputs: true false false true false

카운트 1이 아닌 놈 나오면 바로 나와서 False출력
카운트 1이면 계쏙 수행 후 True 출력

"""

S = "0123456789 01234 01234567890 6789012345 012322456789".split()

for i in range(len(S)):
    S1 = True
    S2 = str(S[i])
    for j in range(10):
        if(S2.count(str(j)) != 1):
            S1 = False
            break
    if(S1 == False):
        print("False", end = " ")
    else:
        print("True", end = " ")

   
