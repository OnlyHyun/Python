"""

앞뒤가 같은 수


10 9 / 90 90 / 900 900 / 9000 9000

1  2   3  4     5   6     7    8
0  1   2  3     4   5     6    7


2로 나눈 후에 10의 제곱승으로 쓴다

첫 번째 자리숫자와 두 번째 자리숫자는 예외로 두자

만약 그 자리숫자에 들게 되면 어떻게 구할 것인가?

무조건 프로그램 반복 횟수의 최소화를 꾀하자

규칙은 한자리 두자리 숫자가 아니라면 

"""

while True:

    n = int(input("n을 입력하시오: "))
    digit = 1
    sum = 19
    
    """ 추잡한가 싶기도 하다 """
    
    if(n < 11) :
        print(n-1)
    elif(n < 20) :
        print(int(str(n%10)*2))
    else :

        while True:

            """
            총 자릿 수가 얼마인지 찾아가기
            """
            digit += 1
            sum += 9 * (10**(digit%2))
            if(sum >= n):

                
                """
                여기서 자릿 수를 좁혀가는 프로그래밍
                n 하고 계속 비교를 해준다
                다음 단계의 숫자와 n을 비교하여 n이 작았을 시에
                그 자리 숫자에 해당하므로 그 숫자를 선정
                
                
    
                """

                break

                    
    if(str(n) == ' '): break 
