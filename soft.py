s = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

"""
1. 김씨와 이씨는 각각 몇 명인가요
2. "이재영"이란 이름이 몇 번 반복되나요?
3. 중복을 제거한 이름을 출력하세요.
4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
"""

name = s.split(',')
lee = 0
kim = 0
l = set(name)

for i in name:
    if i[0] == '이': lee+=1
    elif i[0] == '김': kim+=1

print("이씨는 %d명, 김씨는 %d명" % (lee, kim))

print("이재영은 %d번 반복된다" % name.count('이재영'))

print("중복되지 않는 이름들은 %s" % l)

name = list(l)

print("중복되지 않는 이름들의 오름차순은 %s" % sorted(name))
