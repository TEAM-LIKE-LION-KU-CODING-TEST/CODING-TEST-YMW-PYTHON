import sys

def count_good_words(n, words):
    good_word_count = 0
    
    for word in words:
        stack = []
        for char in word:
            if stack and stack[-1] == char:  # 스택이 비어있다면 else로 넘어간다
                stack.pop()  # 같은 글자끼리 짝을 이루면 스택에서 제거
            else:
                stack.append(char)  # 그렇지 않으면 스택에 추가
        
        if not stack:  # 모든 글자를 돌았을 때, 스택이 비어 있으면 좋은 단어
            good_word_count += 1
    
    return good_word_count

# 입력 처리
n = int(input())  # 단어의 수
inputStr = []
for _ in range(n):
  inputStr.append(sys.stdin.readline().strip())

# 결과 출력
print(count_good_words(n, inputStr))
