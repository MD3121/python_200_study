# 83. 문자열 길이 구하기 (len)

msg = input("임의의 문장을 입력하세요:")
msglen = len(msg)
print("당신이 입력한 문장의 길이는 <%d> 입니다."%msglen)

msglen = len(msg.encode())
print("당신이 입력한 문장의 길이는 <%d> 입니다."%msglen)

'''
python 3 는 모든 문자열ㅇ르 유니 코드로 처리 msg 는 유니 코드로 인식하고 처리한다
encode()는 유니 코드 형식으로 된 문자열을 바이트 객체 형식으로 변환해 줍니다. 사용자가 입력한 문자열을 encode()를 이용해 바이트 객체로 변환하고 이 크기를 msglen()에 대입한 것입니다.
'''