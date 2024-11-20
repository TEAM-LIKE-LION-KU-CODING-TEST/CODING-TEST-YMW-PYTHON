# 2024 11 18
# https://www.acmicpc.net/problem/14891
# 톱니바퀴

word = input("")
suffixes = []
for i in range(len(word)):
    suffixes.append(word[i:])
suffixes.sort()
for i in range(len(suffixes)):
    print(suffixes[i])
