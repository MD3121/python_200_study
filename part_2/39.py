# 39. 함수 이해하기(def)

def add_number(n1, n2):
    ret = n1 + n2
    return ret

def add_txt(t1, t2):
    print(t1 + t2)

ans = add_number(10,15)
print(ans)
text1 = '대한민국 ~'
text2 = '만세!!'
add_txt(text1,text2)

'''
인자와 리턴값이 있는 함수 선언 방법
def 함수이름 (인자1, 인자2, ...):
    코드 ~~~~~~~
    return 결과 값

리턴값은 있지만 인자가 없는 함수 선언 방법
def 함수이름():
    코드들
    return 결과값

인자와 리턴값이 없는 함수 선언 방법
def 함수이름():
    코드들
    return (생략 가능하다)

인자와 리텉값이 있는 함수 호출 방법
변수 = 함수이름(값1, 값2, ...)

리턴값이 없는 함수 호출 방법
함수이름(값1, 값2)

인자와 리턴값이 없는 함수 호출 방법
함수이름()
'''