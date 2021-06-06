# 139. 텍스트 파일을 한줄씩 읽고 출력하기 (readlines)

f = open('stockcode.txt', 'r')
lines = f.readlines()
for line_num, line in enumerate(lines):
   print('%d %s' %(line_num+1, line), end='')
f.close()

'''
텍스트 파일을 한줄 씩 읽는 다른 방법 >> readliens()
텍스트 파일의 끝까지 한줄씩 읽어 각줄을 요소로 하는 리스트로 리턴.
read 와 마찬가지로 텍스트 파일의 모든 내용을 한번에 읽기 때문에 파일 크기가 매우 큰 경우 메모리 문제가 발생  할 수 있으니 주의합니다.


'''