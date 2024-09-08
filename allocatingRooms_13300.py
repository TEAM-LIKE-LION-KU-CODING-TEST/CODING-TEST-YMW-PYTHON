import math

inputStr = input("")
stdntNum, maxnumK = list(map(int, inputStr.split()))


roomList = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

for i in range(stdntNum):
  inputStr = input("")
  intList = list(map(int, inputStr.split()))
  numA, numB = intList
  roomList[numA][numB-1] += 1

# print(roomList)
 
resultNumofRooms = 0
for i in range(2):
  for j in range(6):
    resultNumofRooms += math.ceil(float(roomList[i][j])/maxnumK)

print(resultNumofRooms)