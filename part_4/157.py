# 157. 현재 시간을 년 월 일 시 분 초 로 출력하기 (localtime,strftime)

from time import localtime, strftime

logfile = 'test.log'
def writelog(logfile, log):
   time_stamp = strftime('%Y-%m-%d %X\t', localtime())
   log = time_stamp + log + '\n'

   with open(logfile, 'a') as f:
       f.writelines(log)

writelog(logfile, '2번째 로깅 문장입니다.')


'''
time 모듈은 시간과 관련되어 있는 함수를 제공
localtime()은 대한민국의 현재시간을 time.struct_time 형식의 데이터로 리턴

'''