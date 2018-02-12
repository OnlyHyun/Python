def sum(a, b):
    return a+b

a = b = 10

c = sum(a, b)

print(c)


def say():
    return 'Hi'

print(say())

def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

a = sum_many(1, 2, 3, 4, 5, 6, 7)

print(a)

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")



say_myself('현수', 25)
say_myself('현수', 25, True)
say_myself('현수', 25, False)

a = "현수"
b = "바보"

print(a, b,'\n', a,b)

for i in range(0, 11):
    print(i, end=' ')
