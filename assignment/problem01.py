age = int(input("나이를 입력하세요: "))

if age < 8:
    print("입장료는 0원입니다.")
elif age <= 19:
    print("입장료는 10,000원입니다.")
elif age <= 64:
    print("입장료는 20,000원입니다.")
else:
    print("입장료는 5,000원입니다.")