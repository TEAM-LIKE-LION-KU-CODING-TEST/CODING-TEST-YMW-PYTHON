from collections import deque
import sys

global cyclingDeque
cyclingDeque = deque([])
count = 0
leftCycle = 0
rightCycle = 0

numN, numK = map(int, list(sys.stdin.readline().split()))

for i in range(numN):
    cyclingDeque.append(i+1)

inputStr = sys.stdin.readline()
inputList = list(map(int, inputStr.split()))

#print(cyclingDeque)
# cyclingDeque.rotate(1)
# print(cyclingDeque)

for i in range(numK) :
#    if i == 0:
#        while cyclingDeque[0] != inputList[i]:
#            cyclingDeque.rotate(1)
#            print(f"i==0, inputList[{i}] is {inputList[i]}, deque left : {cyclingDeque[0]}")
#        continue
    
    tempDeque1 = cyclingDeque.copy()
    tempDeque2 = cyclingDeque.copy()
    leftCycle = 0
    rightCycle = 0
    # print(f"temp: {tempDeque} cyc: {cyclingDeque}")
    
    while tempDeque1[0] != inputList[i] :
#        print(f"{tempDeque1}, inputList[i]: {inputList[i]}")
        tempDeque1.rotate(-1)
        leftCycle += 1
#    print(f"leftCycle is : {leftCycle}")
    
    while tempDeque2[0] != inputList[i] :
#        print(f"{tempDeque2}, inputList[i]: {inputList[i]}")
        tempDeque2.rotate(1)
        rightCycle += 1
#    print(f"rightCycle is : {rightCycle}")
    count += min(leftCycle, rightCycle)
    
    if min(leftCycle, rightCycle) == leftCycle:
        cyclingDeque.rotate(-leftCycle)
#        print(f"serched left : leftCycle == {leftCycle}")
    else:
        cyclingDeque.rotate(rightCycle)
#        print(f"serched right : rightCycle == {rightCycle}")
    cyclingDeque.popleft()

print(count)
    
        
        
    
