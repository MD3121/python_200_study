# 77. 문자열에서 홀수 번째 문자만 추출하기

txt = 'aAbBcCdDeEfFgGhHiIjJkKlL'
ret = txt[::2]
print(ret)
ret = txt[1::2]
print(ret)

'''
슬라이싱의 스템을 이용하는 방법

txt[::2] 는 문자열 txt 의 처음부터 끝까지 스텝 2로 슬라이싱 하라는 의미.-
'''