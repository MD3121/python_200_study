# 163.  URL 에서 호스트 도메인 추출하기 

url = 'https://www.youtube.com/feed/subscriptions'

tmp = url.split('/')
domain = tmp[2]
print(domain)
