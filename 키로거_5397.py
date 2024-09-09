numTest = int(input(""))
inputStr = []
resultStr = []
idx = 0
letterFlag = False
for i in range(numTest):
  inputStr = list(input(""))
  resultStr = []
  idx = 0
  for j in range(len(inputStr)):
    print(f"idx is: {idx}")
    if inputStr[j] == '<':
      idx = 0 if idx <= 0 else idx - 1
      letterFlag = False
    elif inputStr[j] == '>':
      idx = len(inputStr)-1 if idx >= len(inputStr) else idx + 1
      letterFlag = False
    elif inputStr[j] == '-':
      if letterFlag == True:
          resultStr.pop()
          idx = 0 if idx <= 0 else idx - 1
      letterFlag = False
    else :
      resultStr.insert(idx, inputStr[j])
      letterFlag = True
      idx = len(inputStr)-1 if idx >= len(inputStr) else idx + 1

      print(f"now the resultStr is : {resultStr} length: {len(resultStr)}")
  print("".join(resultStr))

