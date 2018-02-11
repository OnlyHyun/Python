# 파이썬 문법 배우기

## 숫자 연산

1. 사칙연산은 +, -, *, / 를 사용한다

2. 제곱하는 연산은 ** 을 사용한다

3. 나눗셈 후 나머지를 반환하는 연산자는 %를 사용한다

4. 나눗셈 후 소수점 아랫자리를 버리는 연산자는 //를 사용한다
   > 이 때 음수 -1.75를 //하게 되면 -2 값이 나오게 되는 점에 유의

## 문자열

### 문자열을 만드는 방식은 총 4가지 방법이 있다

1. 큰 따옴표

2. 작은 따옴표

3. 큰 따옴표 3개를 연속으로 써서 둘러싸기

4. 작은 따옴표 3개를 연속으로 써서 양쪽 둘러싸기


### 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 때 쓰는 방법은 3가지 방법이 있다

1. 문자열에 작은 따옴표를 포함시키는 방법은 문자열을 큰 따옴표로 둘러싸는 것이다

	food = "Python's favorite food is perl"
    

2. 문자열에 큰 따옴표를 포함시키는 방법은 문자열을 작은 따옴표로 둘러싸는 것이다.

	say = '"Python is very easy." he says."
    
3. \(백슬래시)를 이용하는 것이다.

	food = 'Python\'s favorite food is perl'
	say = "\"Python is very easy.\" he says."

	> 그냥 편하게 1, 2번 방법을 사용하도록 하자

### 여러 줄인 문자열을 변수에 대입하고 싶을 때

1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기

	multiline = "Life is too short\nYou need python"
	
	> 아무래도 읽기 불편하고 성가시다
	

2. 연속된 작은 따옴표 3개(''') 또는 큰 따옴표 3개(""") 이용

	1) 작은 따옴표 3개 사용

	multiline = '''
	Life is too short
	You need python
	'''
	print(multiline)	
	
	2) 큰 따옴표 3개 사용
	
	Multiline = """
	Life is too short
	You need python
	"""
	print(multiline)		


### 이스케이프 코드란?

> 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다.
주로 출력물을 보기 좋게 정렬하는 용도로 사용된다.

	\n - 개행(줄바꿈)
	\t - 수평 탭
	\\ - 문자 "\"
	\' - 단일 인용부호(')
	\" - 이중 인용부호(")
	\r - 캐리지 리턴
	\f - 폼 피드
	\a - 벨 소리
	\b - 백 스페이스
	\000 - 널문자

### 문자열 연산하기

1. 문자열 더해서 연결하기

	head = "Python"
	tail = " is fun!"
	print(head + tail)
	
	'Python is fun!'

	> 매우 간단 그냥 숫자 더하듯이 + 해주면 된다

2. 문자열 곱하기

	a = "Python"
	print(a * 2)
	
	'PythonPython'

	> 일반적으로 생각하듯이 문자열을 몇 번 반복하라는 의미로 사용된다.

### 문자열 인덱싱

    > 문자열 인덱싱이란 무엇인가를 "가리킨다"라는 뜻이다.

	a = "Life is too short, You need Python"
	
	Life is too short, You need Python
	0	  1	    2	      3
	0123456789012345678901234567890123
	
	print(a[3])

	'e'

	> a[3]이 의미하는 것은 a라는 문자열의 4번째 문자를 말한다. 0부터 시작하는 거에 유의하자
	
	print(a[12], a[-1])
	's', 'n'

	> - 는 뒤에서부터 세는 것이다. [-1]은 끝에서 1번째 자리를 뜻한다

	
### 문자열 슬라이싱

    > 문자열 슬라이싱이란 무엇인가를 "잘라낸다"라는 뜻이다.

	a = "LIfe is too short, You need Python"
	b = a[0] + a[1] + a[2] + a[3]
	print(b)

	'Life'

	> 이 방법은 뽑아내고 싶은 문자가 길어지면 성가신다. 이 것을 해결하는 것이 슬라이싱이다.

	a = "LIfe is too short, You need Python"
	print(a[0:4])
	
	'Life'

	> 간략해진 것을 볼 수 있다. 다만 시작점과 끝점을 표시하는데 끝점은 포함되지 않는다. 즉 0~3번째 까지 표시한다.


#### "Pithon"이라는 문자열을 "Python"으로 바꾸려면?

- 잘못된 예
	
	a = "Pithon"
	print(a[1])
	
	'i'

	a[1] = 'y'

	> 파이썬에서는 문자열 중간의 값만을 수정하는 것은 불가능하다. 문자열의 요소값은 바꿀 수 있는 값이 아니기 때문이다.


- 올바른 예

	a = "Pithon"
	print(a[:1])
	
	'P'

	print(a[2:])
	
	'thon'
	
	print(a[:1] + 'y' + a[2:])

	'Python'

	> 수정할 부분이 양쪽으로 나눠지기 때문에 그 사이에 'y'라는 문자를 추가하여 새로운 문자열을 만들 수 있다.

### 문자열 포매팅

    > 문자열 내에 어떤 값을 삽입하는 것이다.

1. 숫자 바로 대입

	print("I eat %d apples." % 3)
	
	'I eat 3 apples.'

2. 문자열 바로 대입

	print("I eat %s apples." % "five")

	'I eat five apples.'

3. 숫자 값을 나타내는 변수로 대입

	number = 3
	print("I eat %d apples." % number)

	'I eat 3 apples.'

4. 2개 이상의 값 넣기

	number = 10
	day = "three"
	print("I ate %d apples. so I was sick for %s days." % (number, day))
	
	'I ate 10 apples. so I was sick for three days.'

### 문자열 포맷 코드

	%s - 문자열
	%c - 문자1개
	%d - 정수
	%f - 부동소수
	%o - 8진수
	%x - 16진수
	%% - Literal % (문자 % 자체)

	> 1. 유의할 점은 %를 표시하고 싶다면 %%를 이용해야 한다는 것이다
	> 2. %s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있다.(정수든 소수든 문자열로 표현)

### 포맷 코드와 숫자 함께 사용하기

1. 정렬과 공백

	print("%10s" % "hi")

	'        hi'

	print("%-10sjane" % "hi")
 	
	'hi          jane'

2. 소수점 표현하기

	print("%0.4f" % 3.42134234)

	'3.4213'

	print("%10.4f" % 3.42134234)

	'    3.4213'

### 문자열 관련 함수들

1. 문자 개수 세기(count)

	a = "hobby"
	print(a.count('b'))

	2

2. 위치 알려주기1(find)

	a = "Python is best choice"
	print(a.find('b'))

	10

	> 문자가 처음으로 나온 위치를 반환한다. 존재하지 않는다면 -1을 반환한다.

3. 위치 알려주기2(index)

	a = "Life is too short"
	print(a.index('t'))

	8

	> 문자가 처음으로 나온 위치를 반환한다. 존재하지 않는다면 오류가 발생한다.

4. 문자열 삽입

	a = ","
	print(a.join('abcd'))

	'a,b,c,d'

	> abcd라는 문자열의 각각의 문자 사이에 변수 a의 값인 ','를 삽입한다.

5. 소문자를 대문자로 바꾸기(upper)

	a = "hi"
	print(a.upper())

	'HI'

6. 대문자를 소문자로 바꾸기(lower)

	a = "HI"
	print(a.lower())

	'hi'

7. 왼쪽 공백 지우기(lstrip)

	a = " hi "
	print(a.lstrip())
	
	'hi '

8. 오른쪽 공백 지우기(rstrip)

	a = " hi "
	print(a.rstrip())

	' hi'

9. 양쪽 공백 지우기(strip)

	a = " hi "
	print(a.strip())

	'hi'

10. 문자열 바꾸기(replace)

	a = "Life is too short"
	print(a.replace("Life", "Your leg")

	'Your leg is too short'

11. 문자열 나누기(split)

	a = "Life is too short"
	print(a.split())
	
	['Life', 'is', 'too', 'short']
	
	> split 함수에 아무런 값을 넣어 주지 않으면 공백을 기준으로 문자열을 나누어 준다.

	print(a.split(':'))
	
	['a', 'b', 'c', 'd']

	> 괄호 안에 특정한 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다.
	

### 고급 문자열 포매팅

    > 문자열의 format 함수를 이용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

1. 숫자 바로 대입하기

	print("I eat {0} apples".format(3))
	
	'I eat 3 apples'

	> "I eat {0} apples" 문자열 중 {0} 부분이 숫자 3으로 바뀌었다.

2. 문자열 바로 대입하기

	print("I eat {0} apples".format("five"))
	
	'I eat five apples'

	> 문자열의 {0} 항목이 five라는 문자열로 바뀌었다.

3. 숫자 값을 가진 변수로 대입하기

	number = 3
	print("I eat {0} apples".format(number))

	'I eat 3 apples'

	> 문자열의 {0} 항목이 number 변수의 값인 3으로 바뀌었다.

4. 2개 이상의 값 넣기

	number = 10
	day = "three"
	print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

	'I ate 10 apples. so I was sick for three days.'

	> 2개 이상의 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목들이 format 함수의 입력값들로 순서에 맞게 바뀐다. 즉, 위 예에서 {0}은 format 함수의 첫 번째 입력값인 number로 바뀌고 {1}은 format 함수의 두 번째 입력값인 day로 바뀐다.

5, 이름으로 넣기

	print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

	'I ate 10 apples. so I was sick for 3 days.'

	> 위 예에서 볼 수 있듯이 {0}, {1}과 같은 인덱스 항목 대신 더 편리한 {name} 형태를 이용하는 방법도 있다. {name} 형태를 이용할 경우 format 함수의 입력값에는 반드시 name=value와 같은 형태의 입력값이 있어야만 한다. 위 예는 문자열의 {number}, {day}가 format 함수의 입력값인 number=10, day=3 값으로 각각 바뀌는 것을 보여 주고 있다.

6. 인덱스와 이름을 혼용해서 넣기

	print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

	'I ate 10 apples. so I was sick for 3 days.'

	> 위와 같이 인덱스 항목과 name=value 형태를 혼용하는 것도 가능하다.

7. 왼쪽 정렬

	print("{0:<10}".format("hi"))

	'hi        '

	> :<10 표현식을 이용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

8. 오른쪽 정렬

	print("{0:>10}".format("hi"))

	'        hi'

	> 오른쪽 정렬은 :< 대신 :>을 이용하면 된다. 화살표 방향을 생각하면 어느 쪽으로 정렬이 되는지 금방 알 수 있을 것이다.

9. 가운데 정렬

	print("{0:^10}".format("hi"))
	
	'    hi    '

	> :^ 기호를 이용하면 가운데 정렬도 가능하다.

10. 공백 채우기

	print("{0:=^10}".format("hi"))

	'====hi===='

	print("{0:!<10}".format("hi"))

	'hi!!!!!!!!'

	>정렬 시 공백 문자 대신에 지정한 문자 값으로 채워 넣는 것도 가능하다. 채워 넣을 문자 값은 정렬 문자인 <, >, ^ 바로 앞에 넣어야 한다. 위 예에서 첫 번째 예제는 가운데(^)로 정렬하고 빈 공간을 =문자로 채웠고, 두번째 예제는 왼쪽(<)으로 정렬하고 빈 공간을 !문자로 채웠다.

11. 소수점 표현하기

	y = 3.42134234
	print("{0:0.4f}".format(y))

	'3.4213'

	> 위 예는 format 함수를 이용해 소수점을 4자리까지만 표현하는 방법을 보여 준다. 이전에 살펴보았던 표현식 0.4f가 그대로 이용된 걸 알 수 있다.

	print("{0:10.4f}".format(y))

	'    3.4213'
	
	> 위와 같이 자릿수를 10으로 맞출 수도 있다. 역시 58쪽에서 살펴보았던 "10.4f"의 표현식이 그대로 이용된걸 알 수 있다.

12. { 또는 } 문자 표현하기

	print("{{ and }}".format())

	'{ and }'

	> format 함수를 이용해 문자열 포매팅을 할 경우 {나 }와 같은 중괄호(brace) 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 위 예의 {{와 }}처럼 2개를 연속해서 사용하면 된다.

## 리스트 자료형

