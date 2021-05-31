# 119. 리스트 요소 무작위로 섞기(shuffle)

from random import shuffle

listdata = list(range(1, 11))
for i in range(3):
   shuffle(listdata)
   print(listdata)

namelist = ['이승만','윤보선','박정희','최규하', '전두환', '노태우', '김영삼', '김대중', '노무현', '이명박', '박근혜', '문재인']
for i in range(3):
   shuffle(namelist)
   print(namelist)
'''
실행 할 때마다 출력 결과가 달라진다
'''
