# 89. 문자열을 수치형 자료로 변환하기

numstr = input('숫자를 입력하세요: ')
try:
   num = int(numstr)
   print('당신이 입력한 숫자는 정수 <%d>입니다.' %num)
except:
   try:
      num = float(numstr)
      print('당신이 입력한 숫자는 실수 <%f>입니다.' %num) 
   except:
      print('+++ 숫자를 입력하세요~ +++')

'''
input으로 입력 받은 숫자는 문자열로 처리됩니다.
파일 에서 숫자 1234를 읽으면 문자열 '1234'로 읽게 됩니다.
int() float() 이용해 변환 할 수 있다.

'''