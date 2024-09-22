import sys

def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()  # 스택에서 '('를 제거
            else:
                return "NO"  # 스택이 비어 있는데 ')'가 나온 경우
    if not stack:
        return "YES"  # 모든 괄호가 짝지어졌다면 YES
    else:
        return "NO"  # 남아 있는 '('가 있으면 NO

# 입력 처리
t = int(input())  # 테스트 케이스 수
for _ in range(t):
    ps = sys.stdin.readline().strip()
    print(is_vps(ps))  # VPS 여부 출력
