# 138. 텍스트 파일을 한줄씩 읽고 출력하기 (readline)

f = open('stockcode.txt', 'r')
line_num = 1
line = f.readline()
while line:
   print('%d %s' %(line_num, line), end='')
   line = f.readline()
   line_num += 1
f.close()

'''
텍스트 파일의 용량이 매우 클 경우에는read() 로 한꺼번에 파일 내용을 읽어 들이는 것은 메모리 문제가 생길 수 있다.
한줄 단위로 읽는 방법 >> readline()

'''