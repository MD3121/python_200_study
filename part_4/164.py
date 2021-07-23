# 164. URL 에서 쿼리 문자열 추출하기

url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)

'''
? 뒤에 표시되는 문자열을 쿼리 문자열이라 부른다
쿼리 문자열은 " 변수 = 값 " 쌍이 & 로 구분되어 나열된다

'''