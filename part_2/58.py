# 58. 예외처리 이해하기 (try ~ except ~ Exceptioin as e)

try :
    print(param)
except Exception as e:
    print(e)            # name 'param' is not defined 가 출력됨


'''
파이썬은 발생 가능한 예외에 대해 exception 객체로 미리 정의해두고 있는데 이에 대한 내용은 다음 링크에서 확인 가능하다.
https://docs.python.org/3/library/exception.html#bin-exceptions ## 접속 안된다?

except Exception as e 
객체를 e 라는 이름으로 접근 할 수 있게 해줌

실행 결과 : name 'param' is not defined
'''