# 152. 데렉토리 생성하기 (os.mkdir)

import os

newfolder = input('새로 생성할 디렉터리 이름을 입력하세요: ')
try:
   os.mkdir(newfolder)
   print('[%s] 디렉터리를 새로 생성했습니다.' %newfolder)
except Exception as e:
   print(e)


'''
디렉토리를 생성하는 코드2

'''