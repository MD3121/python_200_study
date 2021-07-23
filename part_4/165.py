# 165. 스택 구현하기 (append, pop)

mystack = []

def putdata(data):
   global mystack
   mystack.append(data)

def popdata():
   global mystack
   if len(mystack) == 0:
      return None
   return mystack.pop()
   
putdata('데이터1')
putdata([3, 4, 5, 6])
putdata(12345)

print('<스택상태>: ', end=''); print(mystack)

ret = popdata()
while ret != None:    
    print('스택에서 데이터 추출:', end=''); print(ret)
    print('<스택상태>: ', end=''); print(mystack)
    ret = popdata()

'''
.pop 리스트에서 마지막 요소 삭제 후 마지막 요소만 반환
'''