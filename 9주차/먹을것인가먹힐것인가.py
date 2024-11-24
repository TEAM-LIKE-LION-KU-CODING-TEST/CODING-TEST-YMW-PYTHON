import sys
sys.setrecursionlimit(10**6)

def binary_search(number, searchlist):
    start, end = 0, len(searchlist) - 1
    while start <= end:
        mid = (start + end) // 2
        if searchlist[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return start  # number보다 작은 요소의 개수

numK = int(sys.stdin.readline())
for _ in range(numK):
    numA, numB = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()

    result = 0
    for num in A:
        result += binary_search(num, B)
    print(result)
