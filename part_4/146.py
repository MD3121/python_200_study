# 146. 파일 크기 구하기 (os.path.getsize)

from os.path import getsize

file1 = 'stockcode.txt'
file2 = 'C:/Users/MDY/Desktop/python_200/part_4/img_sample.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s \tFile Size: %d' %(file1, file_size1))
print('File Name: %s \tFile Size: %d' %(file2, file_size2))

'''

'''