from collections import deque

def sliding_window_minimum(n, l, arr):
    dq = deque()  # 최소값을 저장할 deque
    result = []

    for i in range(n):
        # 현재 윈도우에 포함되지 않는 값은 deque에서 제거
        if dq and dq[0] < i - l + 1:
            dq.popleft()
        
        # 새로 들어오는 값보다 큰 값들은 deque에서 제거
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()

        # 현재 인덱스를 deque에 추가
        dq.append(i)

        # 현재 윈도우에서 최소값을 result에 추가
        result.append(arr[dq[0]])

    return result

# 입력 처리
n, l = map(int, input().split())  # n: 배열 길이, l: 윈도우 크기
arr = list(map(int, input().split()))  # 배열 A

# 결과 출력
print(' '.join(map(str, sliding_window_minimum(n, l, arr))))
