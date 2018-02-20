"""
Compression

문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에
그 반복 횟수를 표시하여 문자열을 압축하기.

입력 예시: aaabbcccccca

출력 예시: a3b2c6a1

"""

S = str(input("문자열을 입력하시오: "))

location = 0
count = 1

for i in S:
    if((location+1) == len(S)):
        if(S[location-1] == i):
            print("%c%d" % (i, count), end = "")
        else:
            print("%c%d" % (i, count))
    elif(i == S[location+1]):
        count += 1
    else :
        print("%c%d" % (i, count), end = "")
        count = 1
    location += 1



        
        
