# 46. 파이썬 모듈 임포트 이해하기 (from ~ import)

from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(1)
mylib.add_txt('나는', '파이썬이다')
reverse(1,2,3)

'''
from 모듈이름 import 함수이름
from 패키지 이름 import 모듈이름
'''