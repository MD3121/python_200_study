# 158. 올해 경과된 날짜 수 계산하기 (localtime)

from time import localtime

t = localtime()
start_day = '%d-01-01' %t.tm_year
elapsed_day = t.tm_yday

print('오늘은 [%s]이후 [%d]일째 되는 날입니다.' %(start_day, elapsed_day))

'''
time 모듈은 시간과 관련되어 있는 함수를 제공
localtime()은 대한민국의 현재시간을 time.struct_time 형식의 데이터로 리턴

'''

print("현재 년도",t.tm_year)
print("현재 ㅁ월",t.tm_mon)
print("현재 날짜",t.tm_mday)
print("현재 시간",t.tm_hour)
print("현재 ㅁ분",t.tm_min)
print("현재 ㅁ초",t.tm_sec)
print("섬머 타임일 경우 1. 아닐경우 0 모를경우 -1",t.tm_isdst)
print("",t.tm_mday)
print("현재 요일 0~6 0은 월요일 ",t.tm_wday)
print("1월 1일부터 날짜 수",t.tm_yday)