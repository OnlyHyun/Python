
count1 = int(input("입력할 정수의 개수는? :"))
sum1 = 0

for i in range(count1):
    s1 = int(input(str(i) + "번 정수를 입력하시오 :"))
    sum1 += s1

avg1 = sum1/count1

print("평균은 %d" % avg1)
print("합계는 %d" % sum1)

del sum1, s1, avg1
    
        
