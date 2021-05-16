# 47. 파이썬 모듈 임포트 이해하기 (import ~ as)

import mypackage as mp
import mypackage.mylib as ml

ret1 = mp.mylib.add_txt('대한민국', '1등')
ret2 = ml.reverse(1,2,3)

'''

이름이 긴 모듈에 별명을 붙여 간단하게 호출 가능하다

import 이름이 긴 모듈명 as 별명

이런 방식으로 사용 

import mypackage as mp
위와 같은 경우 mypackage를 mp 로 축약
mypackage.mylib 을 my.mylib으로 축약 가능하다

'''