"""
3n+1 Problem


"""

X, Y = map(int, input("정수 값을 입력하시오: ").split())

Max = 0
    
for i in range(X, Y+1):
     S = i
     Count = 1
     while S != 1:
          if(S%2 == 0):
              S=S/2
              Count+=1
          else: 
              S=S*3+1
              Count+=1

     if(Max < Count): Max = Count
     
print("%-3d %-3d %-3d" % (X, Y, Max))
    
