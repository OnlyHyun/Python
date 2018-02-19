def Dashinsert(left, right):
    if((int(left)%2 == 0) & ((int(right)%2==0))):
        return left+'*'
    elif((int(left)%2==1) & ((int(right)%2==1))):
        return left+'-'
    else:
        return left+''
        
Dash = str(input("문자열을 입력하시오: "))
length = len(Dash)

for i in range(length-1):
    print(Dashinsert(Dash[i],Dash[i+1]),end="")
print(Dash[length-1])
