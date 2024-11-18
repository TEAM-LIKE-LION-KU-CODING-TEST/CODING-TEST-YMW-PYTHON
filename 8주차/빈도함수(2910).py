# 2024 11 18
# https://www.acmicpc.net/problem/2910
# 빈도정렬
import sys
from collections import deque 

Size, MaxNum = map(int, sys.stdin.readline().split())
# print(numbers, maxNum)


Messege = []
Messege.extend(map(int, sys.stdin.readline().split()))

# print(Messege)

Numbers = deque()
Frequency = deque()

for num in Messege:
    if not num in Numbers:
        Numbers.append(num)
        Frequency.append(1)
    else :
        idx = Numbers.index(num)
        Frequency[idx] += 1

#print(Numbers)
#print(Frequency)

result = []
for _ in range(len(Numbers)):
    for j in range(Frequency[_]):
        result.append(Numbers[_])

print(' '.join(map(str, result)))
