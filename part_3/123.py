# 123. 사전에 요소 추가하기

solar1 = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solar2 = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
solardict = {}
for i, k in enumerate(solar1):
   val = solar2[i]
   solardict[k] = val

print(solardict)

'''
딕셔너리에 Key 를 추가하는 방법 >> dict[Key] = 값

'''