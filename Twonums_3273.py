# 240908

# 입력
size = int(input(""))
input_str = input("")
numX = int(input(""))

# 처리
int_list = list(map(int, input_str.split()))
int_list = sorted(int_list, reverse=False)


# print(int_list)

# count : 조건을 만족하는 쌍의 개수
count = 0
sizes = len(int_list)
left = 0
right = sizes - 1

# 예외처리
if sizes < 2:
  print(f"{count}")
else:
  while left < right:
    sum = int_list[left] + int_list[right]
    if sum == numX:
      count += 1
      left += 1
    elif sum < numX:
      left += 1
    else :
      right -= 1
  
print(f"count:{count}")
