#  155. 파일이 존재하는지 체크 (os.path.exists)

import os
from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력하세요: ')
if not exists(dir_name):
   os.mkdir(dir_name)
   print('[%s] 디렉터리를 생성했습니다.' %dir_name)
else:
   print('[%s]은(는) 이미 존재합니다.' %dir_name)

'''
os.path.exiosts()
괄호 안에 해당하는 파일이나 디렉토리가 존재하면 True 존재하지 않으면 False 를 리턴

'''