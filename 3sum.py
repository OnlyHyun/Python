"""
디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

"""

sumSec = 0
for hour in range(24):
    for minute in range(60):
        if '3' in str(hour) or '3' in str(minute):
            sumSec += 60


print(sumSec)
