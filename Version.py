def compare(left, right):
    if(left > right):
        return '>'
    elif(left < right):
        return '<'
    else: '='


S = str(input("첫 번째 버전을 입력하시오: ")).split('.')
S1 = str(input("두 번째 버전을 입력하시오: ")).split('.')

for i in range(3):
    if(compare(S[i], S1[i]) == '<'):
        print(".".join(S), '<', ".".join(S1))
        break
    elif(compare(S[i], S1[i]) == '>'):
        print(".".join(S), '>', ".".join(S1))
        break
    else :
        if(i == 2): print(".".join(S), '=', ".".join(S1))
        else: continue
