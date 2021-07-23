# 180. 남녀 파트너 정해주기 프로그램  ZIP

from random import shuffle

male = ['A', 'B', 'C', 'D', 'E']
female = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ']
shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, couple in enumerate(couples):
   print('커플%d: [%s]-[%s]' %(i+1, couple[0], couple[1]))
