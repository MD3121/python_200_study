# 59. 예외처리 이해하기 (try ~ except 특정 예외)

import time
count = 1

try :
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:           ## Ctrl + C  입력시 발생하는 오류
    print('사용자에 의해 프로그램이 중단되었습니다.')
