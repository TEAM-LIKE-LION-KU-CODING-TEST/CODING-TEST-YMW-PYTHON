Word = input("단어를 입력해주세요:")
LetterArray = []

for i in range(26):
    LetterArray.append(0)

# print(LetterArray)

def get_arrayidx(l):
    ascii_value = ord(l)
    if ascii_value >= 65 and ascii_value <= 90:  # 대문자일 경우
        return ascii_value-65
    elif ascii_value >= 97 and ascii_value <= 122:  # 소문자일 경우
        return ascii_value-97
    else:
        return None  # 알파벳이 아닌 경우 None 반환


for letter in Word:
    print(letter)
    idx = get_arrayidx(letter)
    LetterArray[idx] = LetterArray[idx] + 1

result = " ".join(map(str, LetterArray))
print(result)
