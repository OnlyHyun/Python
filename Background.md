
# Python Background
---
## 1.파이썬이란?
파이썬은 인터프리터 언어이다.
> 인터프리터 언어란 한 줄씩 소스코드를 해석해서 그때그때 실행해 결과를 바로 확인할 수 있는 언어이다.

## 2.파이썬의 특징
- 1. 파이썬은 사람이 생각하는 방식을 그대로 표현할 수 있는 언어이다
- 2. 파이썬은 문법이 쉬워 배우기가 쉽다
- 3. 파이썬은 오픈소스이다
> 오픈 소스란 저작권자가 소스 코드를 공개하여 누구나 별다른 제한 없이 자유롭게 사용,복제,배포,수정할 수 있는 소프트웨어이다. 
- 4. 파이썬은 간결하다


		languages = ['python', 'perl', 'c', 'java']
			
		for lang in languages:
		    if lang in ['python', 'perl']:
		        print("%6s need interpreter" % lang)
		    elif lang in ['c', 'java']:
		        print("%6s need compiler" % lang)
		    else:
		        print("should not reach here")
			
		> 보이듯이 괄호 문자가 보이지 않고 줄을 맞춰야 실행이 되기에 줄이 잘 맞는 것을 볼 수 있다.
