# 71. 정수 리스트에서 소수만 걸러내기 

def getPrime(x):
    if x%2 ==0:
        return

    for i in range(3, int(x/2),2):
        if x%i == 0:
            break
    else:
        return x

listdata = [117,119,1113,11113,11119]
ret = filter(getPrime, listdata)
print(list(ret))


'''
filter(특정 조건의 값을 추출하는 함수, 반복 가능한 자료)

파이썬 내장함수 filter()는 리스트와 같이 반복 가능한 자료에서 특정 조건을 만족하는 값만을 편리하게 추출할 수 있는 방법을 제공합니다. 
filter()의 첫 번쨰 인자는 특정조건의 값을 추출하는 함수가 입려고디며, 두번째 인자는 리스트와 같은 반복 가능한자료가 입력됩니다.

예제는 filter()를 이용해 정수가 담긴 리스트에서 소수만 추출하는 코드입니다.

getPrime() 한수는 인자로 입력된 x 의 값이 소수인지 체크하고 소수일 경우에만 값을 리턴합니다. 
소수를 판단하는 로직은 입력된 수가 홀수인 경우,3 부터 시작하여 입력된 수의 반값까지 한개라도 나누어 떨어지는 수가 있는지 체크하는 것입니다.
여기서 사용된 range()는 순차적인 정수 리스트를 만드는 함수입니다.

5개의 정수를 요소로 가지는 리스트를 정의합니다.
'''