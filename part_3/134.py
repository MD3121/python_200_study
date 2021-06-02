# 134. 문자열로 된 식을 실행하기 (eval)

# expr1 = '2+3'
# expr2 = 'round(3.7)'
expr1 = '2+3*35'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s>를 eval()로 실행한 결과: ' %expr1, end=' '); print(ret1)
print('<%s>를 eval()로 실행한 결과: ' %expr2, end=' '); print(ret2)

'''
수식 또는 문자열을 그대로 실행 해야 되는 경우
두개의 숫자를 더하는 문자열을 텍스트 파일에서 일겅 이를 실행하는 방법
eval()
'''