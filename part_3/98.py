# 98. 문자열을 정렬하기 (sorted, join)

strdata = input('정렬할 문자열을 입력하세요: ')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
ret1 = ''.join(ret1)
ret2 = ''.join(ret2)
print('오름차순으로 정렬된 문자열은 <' + ret1 + '> 입니다.')
print('내림차순으로 정렬된 문자열은 <' + ret2 + '> 입니다.')
