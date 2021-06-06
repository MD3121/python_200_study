# 142. 텍스트 파일 복사하기 (read, wirte)

f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()
