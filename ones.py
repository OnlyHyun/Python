"""
2나 5로 나눌 수 없는 0 이상 10,000 이하의 정수 n이 주어졌는데,
n의 배수 중에는 10진수로 표기했을 때 모든 자리 숫자가 1인 것이 있다.
그러한 n의 배수 중에서 가장 작은 것은 몇 자리 수일까?


바보냐?? 1 11 111 1111 11111 ... 이 나눠지는지 봐
병신같이 풀려면 일일이 배수 곱해서 하면 된다


"""

s = []

while True:

    n = input("0~1000이하의 정수를 입력하시오: ")
    if(n == ' '):
        print("끝 수고!!")
        break
    elif(int(n)%2 == 0 or int(n)%5 == 0):
        print("제대로 입력 안하냐")
        break
    else:
            
        while True:

            s.append('1')

            s1 = "".join(s)
            
            if(int(s1)%int(n) == 0):
                print(len(s1))
                break
    
