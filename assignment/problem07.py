for i in range(1, 31):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("짝!", end=" ")
    else:
        print(i, end=" ")