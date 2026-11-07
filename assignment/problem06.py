password = "python123"

while True:
    user = input("비밀번호를 입력하세요: ")

    if user == password:
        print("로그인 성공! 환영합니다.")
        break
    else:
        print("비밀번호가 틀렸습니다. 다시 입력하세요.")