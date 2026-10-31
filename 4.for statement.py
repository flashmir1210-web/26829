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
        print(key, "not sold out")
        print(key, sale_list[key])



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

# 학생들의 점수를 활용해서
# 1. 개인별 평균점수를 구할것 김철수 nn점 이영희 nn점 ... ->
# 2. 이름으로 검색해서 성적을 알아보기 "김철수" -> {'국어': 85, '영어': 90, '수학': 78, '과학': 92}
# 3. 과목별 최고 득점자 국어 000, 과학 000, 국어 000

class_scores = {
    "김철수": {"국어": 85, "영어": 90, "수학": 78, "과학": 92},
    "이영희": {"국어": 92, "영어": 88, "수학": 95, "과학": 96},
    "박민수": {"국어": 76, "영어": 65, "수학": 82, "과학": 70},
    "정수진": {"국어": 88, "영어": 94, "수학": 90, "과학": 89},
    "한동석": {"국어": 60, "영어": 72, "수학": 65, "과학": 58}
}

# 학생별 평균점수
for name, scores in class_scores.items():
    avg = sum(scores.values()) / len(scores)
    print(name, ":", avg, "점")

# 성적 알아보기 -> 잘못 입력된 케이스 처리
name = input("학생 이름을 입력하세요: ")

if name in class_scores:
    print(name, "의 성적:", class_scores[name])
else:
    print("잘못된 이름입니다. 다시 확인해주세요.")

# 과목별 최고 득점자
subjects = ["국어", "영어", "수학", "과학"]

for subject in subjects:
    best_name = max(class_scores, key=lambda name: class_scores[name][subject])
    best_score = class_scores[best_name][subject]

    print(subject, "최고 득점자:", best_name, best_score, "점")
