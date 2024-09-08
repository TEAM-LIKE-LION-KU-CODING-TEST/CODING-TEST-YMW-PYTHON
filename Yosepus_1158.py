#입력
numN, numK = list(map(int, input("").split()))


yosepusList = []
resultList = []
idx = 0

for i in range(numN):
  yosepusList.append(i+1)

while len(yosepusList) != 0 :
  idx = (idx - 1 + numK) % len(yosepusList)
  temp = yosepusList.pop(idx)
  resultList.append(temp)

result = str(resultList).replace('[', '<').replace(']', '>')
print(result)
  
  

