# 150. 디렉토리에 있는 파일 목록 얻기(os.listdir, glob.glob)

import os, glob

folder = 'C:/Users/MDY/Desktop/python_200'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)
print(file_list)

'''

'''