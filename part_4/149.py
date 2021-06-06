# 149. 파일을 다른 디렉토리로 이동하기 (os.rename)

from os import rename

target_file = 'stockcode.txt'
newpath = input('[%s]를 이동할 디렉터리의 절대경로를 입력하세요: ' %target_file)

if newpath[-1] == '/':
   newname = newpath + target_file
else:
   newname = newpath + '/' + target_file

try:
   rename(target_file, newname)
   print('[%s] -> [%s]로 이동되었습니다.' %(target_file, newname))
except FileNotFoundError as e:
   print(e)

'''
[stockcode.txt]를 이동할 디렉터리의 절대경로를 입력하세요: C:\Users\MDY\Desktop\python_200\part_4
[stockcode.txt] -> [C:\Users\MDY\Desktop\python_200\part_4/stockcode.txt]로 이동되었습니다.
'''