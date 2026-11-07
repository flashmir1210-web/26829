words = {
    "사과": "apple",
    "바나나": "banana",
    "학교": "school"
}

score = 0

for korean in words:
    print(korean, "의 영어 단어는?")
    answer = input("정답: ")

    if answer == words[korean]:
        print("정답입니다! 👍")
        score = score + 1
    else:
        print("아쉬워요, 정답은", words[korean], "입니다.")

print("최종 점수:", score, "점")