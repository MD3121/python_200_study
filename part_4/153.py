# 153. 디렉토리 제거하기 (os.rmdir)

import os

target_folder = '안녕'
k = input('[%s] 디렉터리를 삭제하겠습니까? (y/n)' %target_folder)
if k == 'y':
   try:
      os.rmdir(target_folder)
      print('[%s] 디렉터리를 삭제했습니다.' %target_folder)
   except Exception as e:
      print(e)
