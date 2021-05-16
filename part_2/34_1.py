# 34-1. 문자열 포맷팅 이해하기

from time import sleep
for i in range(100):
    msg = '\r 진행률 %d%%'%(i+1)
    print(''*len(msg),end='')
    print(msg, end='')
    sleep(0.1)