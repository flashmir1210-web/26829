num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
op = input("연산자: ")

if op == "+":
    print("결과:", num1 + num2)
elif op == "-":
    print("결과:", num1 - num2)
elif op == "*":
    print("결과:", num1 * num2)
elif op == "/":
    print("결과:", num1 / num2)
else:
    print("잘못된 연산자입니다.")