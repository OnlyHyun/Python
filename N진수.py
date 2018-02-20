"""

10진수를 n진수로 변환하기

n으로 나눈 나머지와 몫?을 계속 가지고 가야함


"""

def switch(num):
    return{
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
        }.get(num)

Share = int(input("변환할 10진수는?: "))
n = int(input("변환하고 싶은 n진수는?: "))

result = []

while True:

    Remainder = Share%n
    Share = Share//n

    if(Remainder >= 10): Remainder = switch(Remainder)
        
    result.append(Remainder)

    if(Share == 0):
        result.reverse()
        break

    
print(result)
