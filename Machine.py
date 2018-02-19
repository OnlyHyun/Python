"""

가성비 최대화


"""

s = int(input("원래 기계의 가격은?: "))
s1 = int(input("원래 기계의 성능은?: "))
s2 = int(input("추가 부품의 가격은?: "))
s3 = str(input("추가 부품의 성능은?: ")).split()


s3 = sorted(s3)
s3.reverse()
"""

쉽게 하기

s3.sort(reverse=True)
내림차순으로 정렬


"""

for i in s3:
    if((s1/s) < ((s1+int(i))/(s+s2))):
        s+=s2
        s1+=int(i)
    else : break

print(s1//s)


