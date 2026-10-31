a = 0
while a < 10:
    print(a)
    a += 1 # a = a + 1

print("=====================")
print("1. 게임 시작")
print("2. 랭킹 확인")
print("0. 게임종료")
print("=====================")
user_input = None

while user_input != 0:
    user_input = input("원하는 동작을 입력하세요")

    if user_input == "1":
        print("게임을 시작합니다.")
    elif user_input == "2":
        print("랭킹을 확인합니다")
    elif user_input == "0":
        print("게임을 종료합니다.")
    else:
        print("잘못된 입력입니다.")