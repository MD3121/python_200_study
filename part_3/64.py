# 64. 10진수를 16 진수로 변환하기 (hex)

h1 = hex(97)
h2 = hex(98)
ret1 = h1 + h2
print(ret1)
print('h1 = ', h1)
print('h2 = ', h2)

a = int(h1,16)
b = int(h2,16)
ret2 = a + b
print(hex(ret2))
print('a = ', a)
print('b = ', b)

################ 추가 ################
n = 159
print('%X'%n)
print('%x'%n)
''' 
실행 결과 --> 9F 9f
문자열 포맷팅에 사용되는 %X 와 %x 는 16진수를 나타내는 포맷 문자열입니다. 
%X는 16진수를 대문자로 표현하며, %x 는 16진수를 소문자로 표현합니다.
'''

n = 11
print('%02X'%n)
print('%02x'%n)
n = '%05X'%n
print(n)