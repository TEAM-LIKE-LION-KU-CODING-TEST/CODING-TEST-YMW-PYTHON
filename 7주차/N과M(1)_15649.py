# 2024 11 08
# https://www.acmicpc.net/problem/15649
# N과 M(1)
import sys


# 백트래킹 함수
# List : 공백 리스트
# Depth : 현재 깊이
# Visited : 방문 여부 표시

def backTracking(List, Depth, Visited):
    #주어진 깊이에 도달하면 출력 및 종료
    if Depth == numM:
        print(*List)
        return
    
    # 1에서부터 아래로 탐색
    for i in range(1, numN+1):
        if not Visited[i]:
            List.append(i)
            Visited[i] = True
            backTracking(List, Depth+1, Visited)
            List.pop()
            Visited[i] = False

numN, numM = map(int, sys.stdin.readline().split())
Visited  = [False]*(numN+1)

backTracking([], 0, Visited)
