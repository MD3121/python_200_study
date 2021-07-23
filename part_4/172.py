# 172. 인터넷에 있는 이미지를 내 PC 로 저장하기

from urllib.request import urlopen

imgurl = 'https://imgsv.imaging.nikon.com/lineup/dslr/df/img/sample/img_01.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:       
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)
