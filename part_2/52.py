# 52. 클래스 생성자 이해하기

class MyClass:
    def __init__(self):
        self.var = '안녕하세요!'
        print("MyClass 인스턴스 객체가 생성되었습니다")

obj = MyClass()
print(obj.var)

'''

클래스의 인스턴스 객체가 생성될 때 자동적으로 호출되는 메소드가 클래스 생성자입니다. 클래스 생성자는 다음과 같은 이름을 가집니다.
def __init__(self, *args)
## args 는 예제 040에서 설명했던 가변 인자입니다.

'''