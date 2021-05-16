# 24. 논리 연산자 이해하기 (and, or, not)

bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2)  ## False
print(bool1 and bool3)  ## True
print(bool2 or bool3)   ## True
print(bool2 or bool4)   ## False
print(not bool1)        ## False
print(not bool2)        ## True

'''
A and B : A와 B가 모두 참이면 참
A or B  : A,B 중 하나 이상이 참이면 참
not A   : A 논리 값의 반대
'''