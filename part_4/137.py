# 137. 텍스트 파일을 읽고 출력하기(read)

f = open('stockcode.txt', 'r')
data = f.read()
print(data)
f.close()

'''
TXT 파일 다운로드 링크
http://www.infopub.co.kr/index.asp

텍스트 파일 읽기 모드로 파일을 연다. 파일을 여는 방법은 예제 048을 참고
open('stockcode.txt', 'r') >> txt 파일을 읽기모드 'r' 로 오픈하고, 오픈 한 파일을 f 로 지정
f.read 는 stockcode.txt 의 내용을 한번에 읽는다
close() 메소드를 이용해 파일을 닫는다.

'''
