
# 2024 11 18
# https://www.acmicpc.net/problem/14891
# 톱니바퀴

# 톱니바퀴의 상태를 입력받아 저장하고
# 톱니바퀴를 돌리는 함수 rotate(numbering, direction)를 정의
# 명령대로 톱니바퀴를 돌린다.
# 마지막 상태에서 점수를 확인
# 점수를 출력

import sys
from collections import deque 

sawlist = []

def getTwelve(saw) :
    return saw[0]

for _ in range(4) :
    sawlist.append(list(sys.stdin.readline().split()))

#print(sawlist)

saw1 = deque(list(map(int, *sawlist[0])))
saw2 = deque(list(map(int, *sawlist[1])))
saw3 = deque(list(map(int, *sawlist[2])))
saw4 = deque(list(map(int, *sawlist[3])))



def rotate_left(saw):
    return saw.append(saw.popleft())
def rotate_right(saw):
    return saw.insert(0, saw.pop())



visited = [-1, False,False,False,False]

def rotate(n, direction, visited) :
    visited[n] = True
    #print(f"visited: {visited}")
    if n == 1:
        if direction == 1:
            if saw1[2] != saw2[6] and not visited[2] :
                rotate(2, -1, visited)
                #print("2번 톱니를 반시계방향으로 회전시킵니다.")
            rotate_right(saw1)
        elif direction == -1:
            if saw1[2] != saw2[6] and not visited[2] :
                rotate(2, 1, visited)
                #print("2번 톱니를 시계방향으로 회전시킵니다.")
            rotate_left(saw1)
       
                
    elif n == 2:
        if direction == 1:
            if saw2[2] != saw3[6] and not visited[3] :
                rotate(3, -1, visited)
                #print("3번 톱니를 반시계방향으로 회전시킵니다.")
            if saw2[6] != saw1[2] and not visited[1] :
                rotate(1, -1, visited)
                #print("1번 톱니를 반시계방향으로 회전시킵니다.")
            rotate_right(saw2)
                
        elif direction == -1:     
            if saw2[2] != saw3[6] and not visited[3] :
                rotate(3, 1, visited)
                #print("3번 톱니를 시계방향으로 회전시킵니다.")
            if saw2[6] != saw1[2] and not visited[1] :
                rotate(1, 1, visited)
                #print("1번 톱니를 시계방향으로 회전시킵니다.")
            rotate_left(saw2)
            
    elif n==3:
        if direction == 1:
            if saw3[2] != saw4[6] and not visited[4] :
                rotate(4, -1, visited)
                #print("4번 톱니를 반시계방향으로 회전시킵니다.")
            if saw3[6] != saw2[2] and not visited[2] :
                rotate(2, -1, visited)
                #print("2번 톱니를 반시계방향으로 회전시킵니다.")
            rotate_right(saw3)
                
        elif direction == -1:
            if saw3[2] != saw4[6] and not visited[4] :
                rotate(4, 1, visited)
                #print("4번 톱니를 시계방향으로 회전시킵니다.")
            if saw3[6] != saw2[2] and not visited[2] :
                rotate(2, 1, visited)
                #print("2번 톱니를 시계방향으로 회전시킵니다.")
            rotate_left(saw3)
                
    elif n == 4:
        if direction == 1:
            if saw4[6] != saw3[2] and not visited[3] :
                rotate(3, -1, visited)
                #print("3번 톱니를 반시계방향으로 회전시킵니다.")
            rotate_right(saw4)
        elif direction == -1:
            if saw4[6] != saw3[2] and not visited[3] :
                rotate(3, 1, visited)
                #print("3번 톱니를 시계방향으로 회전시킵니다.")
            rotate_left(saw4)
            
    else:
        print("Direction Error!")
    return

#print(f"saw1: {saw1})")
#print(f"saw2: {saw2})")
#print(f"saw3: {saw3})")
#print(f"saw4: {saw4})")

numK = int(input(""))
for _ in range (numK):
    order, direction = map(int, sys.stdin.readline().split())
    visited = [-1, False,False,False,False]
    rotate(order, direction, visited)

#print(f"saw1: {saw1})")
#print(f"saw2: {saw2})")
#print(f"saw3: {saw3})")
#print(f"saw4: {saw4})")

point = 0
if getTwelve(saw1) :
    point += 1
if getTwelve(saw2) :
    point += 2
if getTwelve(saw3) :
    point += 4
if getTwelve(saw4) :
    point += 8

print(point)
