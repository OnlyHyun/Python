inz = str(input("인용 횟수를 입력하시오: ")).split()

inz = list(map(int, inz))
inz.sort(reverse = True)

sum = 0
count = 0
h_index = 0
g_index = 0

for i in inz:
    sum += i
    count += 1
    if((count >= h_index) & (i >= h_index)): h_index = count    
    if((count >= g_index) & (sum >= count**2)): g_index = count

"""
&문 쓸 때 우선연산자 조심해서 하자ㅜㅜ
괄호 다 쳐줘라

"""


print("h_index : %d g_index : %d" % (h_index, g_index))
