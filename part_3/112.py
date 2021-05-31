# 112. 리스트에서 특정 요소 제거하기 (remove)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solarsys.remove('태양')
print(solarsys)

'''
리스트에서 특정 값을 미리 알고 있다면 .remove() 이용하여 제거 할 수 있다

만약 리스트에 존제하지 않는 요소를 제거하려고 시도 시 다음과 같은 오류가 발생
    ValueError: list.remove(x): x not in list

'''