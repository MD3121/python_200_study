# 143. 바이너리 파일 복사하기

bufsize = 1024
f = open('img_sample.jpg', 'rb')
h = open('img_sample_copy.jpg', 'wb')

data = f.read(bufsize)
while data:
   h.write(data)
   data = f.read(bufsize)

f.close()
h.close()

'''
일반적으로 바이너리 파일은 용량이 큰 경우가 많다. 
이런 '경우 파일을 처음부터 끝까지 일정한 크기 단위로 읽고 쓰면 메모리 문제를 해결 할 수 있다.

bufsize 를 1024 로 정의합니다 .1024 = 1KB 파일을 일긱 위해서 정의한 값 (1024byte  만큼 읽는 다는 뜻)
만약 파일을 256KB 로 읽고 싶은 경우에는  bufsize  = 256 * 1024 로 정의하면 됩니다.

'''