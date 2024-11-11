# 2024 11 11
# https://www.acmicpc.net/problem/1992
# 쿼드트리
import sys

def quadTree(x, y, size, data):
    head = data[x][y]
    all_same = True
    for i in range(x, x+size):
        for j in range(y, y+size):
            if data[i][j] != head:
                all_same = False
                break
        if all_same == False:
            break

    if all_same == True:
        return head

    else:
        half_n = size // 2
        top_left = quadTree(x, y, half_n, data)
        top_right =quadTree(x, y + half_n, half_n, data)
        bottom_left = quadTree(x + half_n, y, half_n, data)
        bottom_right = quadTree(x + half_n, y + half_n, half_n, data)

        result  = f"({top_left}{top_right}{bottom_left}{bottom_right})"

        return result


numN = int(sys.stdin.readline().strip())
videoData = [list(map(int, sys.stdin.readline().strip())) for _ in range(numN)]

print(quadTree(0, 0, numN, videoData))
