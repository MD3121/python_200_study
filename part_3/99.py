# 99. 순차적인 정수 리스트 만들기(range)

range1 = range(10)
range2 = range(10, 20)
print(list(range1))   # [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9] 출력
print(list(range2))   # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 출력

'''
순차적인 정수 리스트를 만드는 간단한 방법 range()
range(10) >> 0 이상 10 미만
range(10, 20) >> 10 이상 20 미만 정수
'''

ret = 0
for i in range(10):
    ret += (i+1)
    print(ret)