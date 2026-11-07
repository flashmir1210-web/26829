numbers = [12, 7, 19, 20, 33, 42, 8, 15, 26, 31]

count = 0

for num in numbers:
    if num % 2 == 0:
        print("짝수:", num)
        count = count + 1

print("총 짝수 개수:", count, "개")