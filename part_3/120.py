# 120. 리스트의 모든 요소를 인덱스와 쌍으로 추출하기 (enumerate)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
ret = list(enumerate(solarsys))
print(ret)

for i, body in enumerate(solarsys):
   print('태양계의 %d번째 천체: %s' %(i, body))

namelist = ['이승만','윤보선','박정희','최규하', '전두환', '노태우', '김영삼', '김대중', '노무현', '이명박', '박근혜', '문재인']
ret = list(enumerate(namelist))
print(ret)

for i, name in enumerate(namelist):
    print(' %d 번째 대통령 : %s'%(i+1,name))