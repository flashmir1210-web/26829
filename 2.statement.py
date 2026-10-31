if True:
    print("True")
    print("True라면 내부는 모두 수행합니다.")

if False:
    print("false")
    print("false라면 내부는 모두 수행하지 않습니다.")

print("Always")

var1 = 1

var2 = 2

if var1 > var2:
    print("var1이 더 큽니다.")

if var1 == var2:
    print("var1과 var2가 같습니다.")

if var1 < var2:
    print("var2가 더 큽니다")

print("=====================")
print("1. 게임 시작")
print("2. 랭킹 확인")
print("0. 게임종료")
print("=====================")
user_input = input("원하는 동작을 입력하세요")

if user_input == "1":
    print("게임을 시작합니다.")




# 사용자에게 숫자와 연산자를 입력받아서 결과를 출력하는 프로그램

number1 = input("첫번째 숫자를 입력하세요: ")
number2 = input("두번째 숫자를 입력하세요: ")
operator = input("연산자를 입력하세요 (+, -, *, /): ")

# 입력받은 문자열을 숫자로 변환
number1 = float(number1)
number2 = float(number2)

# 연산자에 따른 계산
if operator == "+":
    result = number1 + number2

elif operator == "-":
    result = number1 - number2

elif operator == "*":
    result = number1 * number2

elif operator == "/":
    if number2 == 0:
        print("0으로 나눌 수 없습니다.")
        result = None
    else:
        result = number1 / number2

else:
    print("잘못된 연산자입니다.")
    result = None

# 계산 결과 출력
if result is not None:
    print("계산 결과:", result)
