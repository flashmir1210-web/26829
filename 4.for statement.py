arr = ["apple", "banana", "cherry"]
print("메뉴 리스트")
for item in arr:
    print(item)

print("------------------")
print("메뉴 리스트")
sale_list = {'apple': 1, 'banana': 0, 'cherry': 3}
for key in sale_list:
    if sale_list[key] == 0:
        print(key, "sold out")
    else:
        print(key, "not sold out")print(key, sale_list[key])




print("------------------")
for i in range(10):
    print(i)
"""
# while 문으로 동일하게 수행하려면
a = 0
while a < 10:
    print(a)
    a += 1 
"""


print("--------------")
ex_arr = [num for num in range(10)]
print(ex_arr)