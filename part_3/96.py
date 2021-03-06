# 96. 문자열을 바이트 객체로 바꾸기 (encode)

u_txt = 'I love python'
b_txt = u_txt.encode()
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)    # True 출력
print(ret2)    # False 출력

'''
바이트 객체는 2진 스트림 데이터로써 컴퓨터의 메모리에 기록되는 값으로 이해하면 됩니다.

예를 들어, 알파벳 대문자 'I' 에 해당되는 코드 값은 73입니다.
대문자 'I'는 컴퓨터 메모리에 73 이라는 정수 값을 기록 됩니다.
파이썬 3 에서 모든 문자열은 유니 코드 문자열로 취급되며, 문자열 'I' 가 컴퓨터 메모리에 기록되는 바이트
객체의 값은 정수 73 입니다. 
문자열 객체의 encode() 메소드는 유니코드로 되어 있는 문자열을 인자로 지저오딘 인코딩 방식으로 인코딩 하여 바이트 객체로 변환합니다.
encoe() 에 인자가 없으면 디폴트로 "UTF-8"로 인코딩한 바이트 객체로 변환합니다.

'''