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


# 빈도 정렬
combined = list(zip(Numbers, Frequency))
combined.sort(key = lambda x: -x[1])        # lambda식, -x[] 표현은 역순으로 정렬을 의미한다)
Numbers, Frequency = zip(*combined)



#print(Numbers)
#print(Frequency)

result = []
for _ in range(len(Numbers)):
    for j in range(Frequency[_]):
        result.append(Numbers[_])

print(' '.join(map(str, result)))
