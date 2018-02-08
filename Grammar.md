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

