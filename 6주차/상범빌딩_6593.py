# 드림학기제, 종합설계 중간 발표 준비로 시간이 부족해 GPT했습니다..

from collections import deque



# 여섯 가지 방향 벡터
directions = [
    (0, 0, 1), (0, 0, -1),  # 동, 서
    (0, 1, 0), (0, -1, 0),  # 남, 북
    (1, 0, 0), (-1, 0, 0)   # 상, 하
]

# start 배열은 현재의 위치를 [l, r, c]로 저장하는 크기 3의 배열

def escape_building(L, R, C, building, start, end):
    # 시작 위치와 초기 시간(분)을 큐에 저장
    # *start => 언패킹 
    queue = deque([(*start, 0)])  
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]

    # start
    visited[start[0]][start[1]][start[2]] = True

    # 방문 큐
    while queue:
        # 언패
        z, x, y, minutes = queue.popleft()

        # 출구에 도달했을 경우
        if (z, x, y) == end:
            return f"Escaped in {minutes} minute(s)."

        # 6방향 탐색
        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy

            # 범위 내에 있고, 방문하지 않았으며, 이동 가능한 곳인지 확인
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                # not visited[nz][nx][ny] : 아직 방문하지 않았으며
                # building[nz][nx][ny] 
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny, minutes + 1))

    # 출구에 도달하지 못한 경우
    return "Trapped!"


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = end = None

    for l in range(L):
        floor = []
        for r in range(R):
            line = input().strip()
            floor.append(line)
            for c in range(C):
                if line[c] == 'S':
                    start = (l, r, c)
                elif line[c] == 'E':
                    end = (l, r, c)
        building.append(floor)
        input()  # 빈 줄 제거

    # 결과 출력
    print(escape_building(L, R, C, building, start, end))
