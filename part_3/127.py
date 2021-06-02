# 127. 사전에서 키만 추출하기 (Keys)

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 
'Michale':27115, 'Bob':5887, 'Kelly':7855}
ks = names.keys()
print(ks)
print(list(ks))
for k in ks:
   print('Key:%s \tValue:%d' %(k, names[k]))

'''
.keys()
딕셔너리의 키 값만 뽑는 방법 리스트 형식
'''