# 50. 클래스 멤버와 인스턴스 멤버 이해하기

class MyClass:
    var = '안녕하세요'
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
# obj.param1

'''
클래스 안에서 선언되는 변수는 클래스 멤버와 인스턴스 멤버가 있습니다.
클래스 멤버는 클래스 메소드 바깥에서 선언되고 인스턴스 멤버는 클래스 메소드 안에서 self. 와 함께 선언되는 변수입니다.

Myclass 내에서 var라는 이름의 변수를 선언했습니다. 이 변수는 클래스 메소드 바깥에서 선언되었으므로 클래스 멤버가 됩니다.
클래스 멤버 var 는 다음과 같이 참조할 수 있습니다.
self.var    # 클래스 메소드 내에서 var 를 참조할 경우
MyClass.var # 클래스 밖ㅆ에서 클래스 이름만으로 참조할 경우(별로 사용 안하는 방식이다)
obj.var     # MyClass의 인스턴스 객체 obj 에서 var 를 참조할 경우
'''