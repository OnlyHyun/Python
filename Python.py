print("주식은 대박이다.")
print("I love 'you'")
print("I like you")
print('Korea')

def sum(Daum, Dnumber, Naver, Nnumber):
    return Daum * Dnumber + Naver * Nnumber

total = sum(89000, 100, 751000, 20)

print(total, '원')


Daum = int(input("다음의 주가는? :"))
Dnumber = int(input("다음 주식 보유숫자는? :"))
Dtotal = Daum * Dnumber

Naver = int(input("네이버의 주가는? :"))
Nnumber = int(input("네이버 주식 보유숫자는? :"))
Ntotal = Naver * Nnumber

total = Daum * Dnumber + Naver * Nnumber

print(total, "원")

lose = Dtotal- Dtotal*0.95 + Ntotal - Ntotal*0.9

print(lose)


F = 50
C = (F-32)/1.8

print(C)

print("Pizza"*10)

Ntotal = 1000000

Ntotal = Ntotal*(0.7**3)




print(Ntotal)
