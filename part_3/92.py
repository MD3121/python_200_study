# 92. 문자열에 있는 문자 (열) 위치 찾기 (find )

txt = 'A lot of things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print(offset1)   # 22 출력
print(offset2)   # 27 출력
print(offset3)   # 38 출력

'''
find() 문자열에서 특정 문자나 문자열이 위치하는 인덱스를 리턴합니다.

'''