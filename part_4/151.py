# 151. 현재 디렉토리 확인하고 바꾸기 (os.getcwd, os.chdir)

import os

pdir = os.getcwd()
print(pdir)

os.chdir('..')
print(os.getcwd())

os.chdir(pdir)
print(os.getcwd())

'''
현재 작업하고 있는 디렉토리의 부모 디렉토리로 작업 공간을 변경하고 다시 자신의 디렉토리로 돌아오는 코드

'''