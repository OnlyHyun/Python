"""
Every Other Digit

def isNumber(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
S = str(input("문자열을 입력하시오: " ))
count = 1

for i in S:
    if(count%2 == 0 and isNumber(i)):
        print("*",end="")
        count+=1
    else:
        print(S[count-1],end="")
        count+=1
    
"""


S = list(input("문자열을 입력하시오: " ))

for i in range(1, len(S), 2):
    if S[i].isdigit():
        S[i] = "*"

print("".join(S))

