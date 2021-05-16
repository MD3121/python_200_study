# for 문 개념 배우기(for)

scope = [1,2,3,4,5]
for x in scope:
    print(x)
'''
for 문 사용 가능 한 것은 자료 형 또는 반복 가능한 자료 이어야 하며 다음과 같은 객체 들이 있습니다.
1. 문자열
2. 리스트 or 튜플
3. 사전 (딕셔너리)
4. range()
5. 그 외 반복 가능한 객체
'''
str='abcdef'
print('문자열')
for c in str:
    print(c) 
'''
문자열 범위로 지정
a/b/c/d/e/f 순서대로 출력
'''
list=[1,2,3,4,5]
print('리스트')
for c in list:
    print(c)
'''
리스트를 범위로 지정
1/2/3/4/5 순서대로 출력
'''
acii_codes={'a':97,'b':98,'c':99}
print('사전')
for c in acii_codes:
    print(c) 
'''
딕셔너리를 범위로 지정
a/b/c key 값이 순서대로 출력
'''
print('range 값')
for c in range(10):
    print(c) 
'''
딕셔너리를 범위로 지정
0~9까지 10개의 값이 순서대로 출력
'''