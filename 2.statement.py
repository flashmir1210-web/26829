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