# 49. 클래스 이해하기 (class)

class Myclass:
    var = '안녕하세요'
    def sayHello(self):
        print(self.var)

obj = Myclass()
print(obj.var)
obj.sayHello()

'''
class 클래스 이름:
    클래스 멤버 정의
    클래스 메소드 정의
'''