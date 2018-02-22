S = str(input("입력: ")).split()

C = int(S.pop(0))

C = C % (len(S))
S = S[-C:] + S[:-C]
    
print(" ".join(S))
