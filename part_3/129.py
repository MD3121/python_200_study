# 129. 사전에서 요소를 모두 추출하기

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 
'Michale':27115, 'Bob':5887, 'Kelly':7855}
items = names.items()
print(items)
print(dict(items))
print(dict(items)['Mary'])
print(list(items))
print(list(items)[0])
for item in items:
   print(item)

