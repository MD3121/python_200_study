# 131. 사전 정렬하기 (sorted)

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 
'Michale':27115, 'Bob':5887, 'Kelly':7855}
ret1 = sorted(names)
print(ret1)

def f1(x):
   return x[0]

def f2(x):
   return x[1]

ret2 = sorted(names.items(), key=f1)
print(ret2)

ret3 = sorted(names.items(), key=f2)
print(ret3)

ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)

'''
sorted() 는 사전 자료를 인자로 입력받아 정렬 할 수 있습니다.

'''