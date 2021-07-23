# 156. 파일인지 디렉토리인지 확인하기 (os.path.isfile, os.path.isdir)

import os
from os.path import isdir, isfile

files = os.listdir()
for file in files:
   if isdir(file):
      print('DIR: %s' %file)

for file in files:
   if isfile(file):
      print('FILE: %s' %file)

'''
os.path.isfile()
입력된 경로가 파일이면 True, 파일이 아니면 False 를 리턴

os.path.isdir()
입력된 경로가 디렉토리이면 True, 디렉토리가 아니면 False 를 리턴

'''