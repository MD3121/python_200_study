# 122. 리스트 요소가 모두 참인지 확인하기 (all, any)

listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1))   # False
print(any(listdata1))   # True
print(all(listdata2))   # True
print(any(listdata2))   # True
print(all(listdata3))   # False
print(any(listdata3))   # False

'''
all() >> 모든 요소가 참인지 판단, 리스트의 모든 구성 요소가 참이여야함
any() >> 참인 요소가 있는지 판단, 리스트의 모든 구성 요소가 거짓이여야 False 를 리턴 아니면 True

파이썬 내부에서 거짓 의미 하는 값
숫자        0
빈 문자열   ""
빈 리스트   []
빈 튜플     ()
빈 사전     {}
None


'''