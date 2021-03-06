"""
아이들은 여러 자리 숫자들을 더하기 위해서 우에서 좌로 숫자를 하나씩
차례대로 더 하라고 배웠다. 1을 한 숫자 위치에서 다음 자리로 더하기위해
이동하는 "한자리올림"연산을 많이 발견하는 것은 중요한 도전이 된다.
당신의 일은 교육자가 그들의 어려움을 평가하기 위하여, 덧셈 문제들의
각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.

자릿 수가 어떤 놈들이 더 큰지?
-1부터 끝까지 해서

--> 그럴 필요 없음 그냥 무한루프에다가 %10 해서 깎은 거 넣어주면 됨

긴 놈 기준으로 해야 하나?

  
2가 되는 거잖냐? 예외 처리 해야 하나? 



"""

while True:

    S = list(map(int, input("양의 정수 두 개를 입력하시오: ").split()))

    if(S[0] == 0 and S[1] == 0): break
    s0, s1 = len(str(S[0])), len(str(S[1]))
    
    
    if(s0 < s1):
        min, S[0], S[1] = s1, S[1], S[0]
    else: min = s0
    count = 0


    for i in range(0,min-1):
        if(S[0]%10 + S[1]%10 > 9):
            count += 1
        S[0] /= 10
        S[1] /= 10

    if(S[0]%10 + S[1]%10 > 9):
        count += 1
        S[0] /= 10
        if(S[0]%10 == 9): count += 1

    if count:
        print("%d carry operation" % count)
    else:
        print("No carry operation")            


    
