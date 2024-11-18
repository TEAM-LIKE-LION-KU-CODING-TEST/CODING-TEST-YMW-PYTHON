# 2024 11 18
# https://www.acmicpc.net/problem/14499
# 주사위굴리기

import sys

numN, numM, startX, startY, commands = map(int, sys.stdin.readline().split())

Map = [[0] * numM for _ in range(numN)]
#print(Map)

for i in range(numN):
    inputlist = list(map(int, sys.stdin.readline().split()))
    for j in range(numM):
        Map[i][j] = inputlist[j]

#print(f"inputMap : {Map}")

Commands = list(map(int, sys.stdin.readline().split()))

diceState = [2, 4, 1, 3, 5 ,6]

# 이동 방향 정의 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def getTop():
    return diceState[2]
def getBottom():
    return diceState[5]

def rollRight():
    temp = diceState[3]
    diceState[3] = diceState[2]
    diceState[2] = diceState[1]
    diceState[1] = diceState[5]
    diceState[5] = temp
    return
def rollLeft():
    temp = diceState[1]
    diceState[1] = diceState[2]
    diceState[2] = diceState[3]
    diceState[3] = diceState[5]
    diceState[5] = temp

def rollUp():
    temp = diceState[0]
    diceState[0] = diceState[2]
    diceState[2] = diceState[4]
    diceState[4] = diceState[5]
    diceState[5] = temp

def rollDown():
    temp = diceState[5]
    diceState[5] = diceState[4]
    diceState[4] = diceState[2]
    diceState[2] = diceState[0]
    diceState[0] = temp


def roll(num):
    if num == 1:
        rollRight()
    elif num == 2:
        rollLeft()
    elif num == 3:
        rollUp()
    elif num == 4 :
        rollDown()
    else :
        print("dice Error!!")

x, y = startX, startY
for command in Commands:
    # 이동할 좌표 계산
    nx, ny = x + dx[command - 1], y + dy[command - 1]

    # 지도 밖으로 이동하면 명령 무시
    if nx < 0 or nx >= numN or ny < 0 or ny >= numM:
        continue

    # 위치 갱신
    x, y = nx, ny

    # 주사위 굴리기
    roll(command)

    # 지도와 주사위 바닥 숫자 동기화
    if Map[x][y] == 0:
        Map[x][y] = diceState[5]  # 주사위 바닥 숫자를 지도에 복사
    else:
        diceState[2] = Map[x][y]  # 지도의 숫자를 주사위 바닥으로 복사
        Map[x][y] = 0  # 지도 숫자는 0으로 초기화

    # 주사위 윗면 출력
    print(diceState[2])
    



