# 88. 문자열에서 좌우 공백 제거하기 (istrip, rstrip, strip)

txt = '   양쪽에 공백이 있는 문자열입니다.   '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<'+txt+'>')
print('<'+ret1+'>')
print('<'+ret2+'>')
print('<'+ret3+'>')

'''
1. .lstrip()
    문자열 객체의 lstrip() 메ㅔ소드는 문자열에 존재하는 왼쪽 공백을 제거한 후 결과를 리턴합니다.
    ret1 은 txt 의 왼쪽 공백이 제거된 문자열이 됩니다.

2. .rstrip()
    문자열 객체의 .rstrip() 메소드는 문자열에 존재하는 오른 쪽 공백을 제거한 후 결과를 리턴합니다.
    ret1 은 txt 의 오른쪽 공백이 제거된 문자열이 됩니다.

3. .strip()
    문자열 객체의 strip() 메소드는 문자열에 존재하는 왼쪽, 오른쪽 공백을 모두 제거한 결과를 리턴합니다.

.lstrip() >> 왼쪽 공백
.rstrip() >> 오른쪽 공백
.strip()  >> 좌 우 공백

'''