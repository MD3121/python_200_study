# 62. 나누셈에서 나머지만 구하기 (%)

a = 11113
b = 23
ret = a%b
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.'%(a,b,ret))

'''
코드 실행 결과 --> <11113>를 <23>로 나누면 <4>가 나머지로 남습니다.

나누기 연산에서 나머지만 구하는 연산을 모듈로 ( modulo )연산이라 하며 기호는 mod 로 표시합니다. 
예를 들어 12는 3으로 나누어 떨어지므로 나머지가 0 이 되며, 12를 5로 나누면 나머지는 2가 됩니다.
이를 수학시긍로 표현하면 다음과 같습니다 
12 mod 3 = 0
12 mod 5 = 2
12 % 3 = 0
12 % 5 = 2
'''