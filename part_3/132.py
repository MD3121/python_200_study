# 132. 문자 코드값 구하기 (ord)

ch = input('문자를 1개 입력하세요: ')
if len(ch) != 0:
   ch = ch[0]
   chv = ord(ch)
   print('문자: %s \t코드값: %d [%s]' %(ch, chv, hex(chv)))

'''
파이썬 내장 함수 oord()
문자를 컴퓨터가 인식하는 코드값으로 변환합니다.
'''