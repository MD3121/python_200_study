# 171. URL 에 접속하여 HTML  페이지를 파일로 저장하기

from urllib.request import urlopen

url = 'https://www.google.com'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('gogle.html', 'w') as h:
        h.writelines(doc)
