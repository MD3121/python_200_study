# 145. 파일의 특정 부분만 복사하기 (seek, read, write)

spos = 99    # 파일을 읽는 위치 지정
size = 1000    # 읽을 크기를 지정

f = open('stockcode.txt', 'r')
h = open('stockcode_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()

'''
open()으로 파일을 열면 파일을 읽거나 쓰는 위치는 파일의 제일 첫 부분으로 고정
파일을 읽는 위치를 임의로 이동하려면 파일 객체의 seek()이용하면 됩니다.
stockcode.txt 의 105 바이트 위치부터 500 바이트를 읽어 그내용을 'stockcode_part.txt' 에 저장 하는 코드

spos 는 파일을 읽는 위치 와 Size 는 파일을 읽을 크기를 지정한 변수입니다.

'''