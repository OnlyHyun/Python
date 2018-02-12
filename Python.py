s = "Daum KaKao"

print(s)

a = s[0:4]
b = s[5:]

s = b + a

print(s)

a = "Hello world"

a = "hi world"

print(a)

x = "abcdef"

x = 'bcdefa'

print(x)

naver_end_price = [['09/07', "월", 474500], ['09/08', "화", 461500], ['09/09', "수", 501000], ['09/10', "목", 500500], ['09/11', "금", 488500]]

print(naver_end_price[1])
print(max(naver_end_price))
print(min(naver_end_price))
print("수요일 종가는", naver_end_price[2][2])


naver_end_price2 = {"09/07":474500, "09/08":461500, "09/09":501000, "09/10":500500, "09/11":488500}

print(naver_end_price2["09/09"])


for key, name in naver_end_price2.items():
    print(key, name)


for i in range(0,5):
    print("*", end = " ")
print(" ")

for i in range(0, 4):
    for j in range(0, 5):
        print("*", end = " ")
    print(" ")


""" 반복 횟수 1,2,3,4,5 """

for i in range(1, 6):
    for j in range(0, i):
        print("*", end = " ")
    print(" ")


for i in range(1, 6):
    for j in range(0, 6-i):
        print("*", end = " ")
    print(" ")


for i in range(1, 6):
    for j in range(0, 5-i):
        print(" ", end = " ")
    for j in range(0, i):
        print("*", end = " ")
    print(" ")

for i in range(0, 5):
    for j in range(0, i):
        print(" ", end = " ")
    for j in range(0, 5-i):
        print("*", end = " ")
    print(" ")   

for i in range(1, 6):
    for j in range(0, 5-i):
        print(" ", end = " ")
    for j in range(0, i*2-1):
        print("*", end = " ")
    for j in range(0, 5-i):
        print(" ", end = " ")
    print(" ")

for i in range(0, 5):
    for j in range(0, i):
        print(" ", end = " ")
    for j in range(0, 9-2*i):
        print("*", end = " ")
    for j in range(0, i):
        print(" ", end = " ")
    print(" ")



4, 1, 4
3, 3, 3
2, 5, 2
1, 7, 1
0, 9, 0
