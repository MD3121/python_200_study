# 75. 문자열에서 특정 위치의 문자 얻기

txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
print(txt1[3:7])
print(txt1[:6])
print(txt2[-4:])

txt = 'python'
for i in range(len(txt)):
    print(txt[:i+1])