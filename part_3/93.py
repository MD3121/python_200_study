# 93. 문자열을 특정 문자(열)로 분리하기 (split)

url = 'http://www.naver.com/news/today=20160831'
log = 'name:문대영 age:25 sex:남자 nation:korea'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()
for data in ret2:
   d1, d2 = data.split(':')
   print('%s -> %s' %(d1, d2))

'''
코드를 작성할 때 가장 많이 접하게 되는 경우가 구분자 (separator)로 구분되어 있는 문자열을 파싱 하는 일.
이때 문자열 객체의 split()을 활용 하ㅣㅣ여 구분자를 기준으로 문자열을 쉽게 분리하여 파싱 할 수 있습니다.
'''