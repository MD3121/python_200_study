# 14. while 문 개념 배우기 (while ~ continue ~ break)

x = 0
while x < 10:
    x =x+1
    if x<3:
        continue ## while 문 처음 으로 이도앟여 반복문 계속 
    print(x)
    if x>7:
        break ## while 문 탈출 조건