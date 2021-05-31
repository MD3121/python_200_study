# 110. 리스트의 특정 위치에 요소 삽입하기(insert)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print(solarsys)

'''
예제 :
목성이 위치의 list index 를 pos 로 뽑아서 그 위치의 '목성' 을 '소행성' 을 추가하고 '목성' 뒤의 요소는 index 가 1 만큼 밀려난다. 
'''