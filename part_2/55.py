# 55. 예외 처리 이해하기 (try ~ except)

try :
    print("안녕하세요")
    # print(param)
except:
    print("예외가 발생")

'''

뜻하지 않은 오류 발생시 예외 처리 하여서 게속 프로그램이 진행 가능하도록 하는 구문

위의 예제의 경우 예외 처리 안하면 다음과 같은 오류가 발생한다
NameError: name 'param' is not defined
parma 이 정의가 되어있지 않기 떄문이다

'''