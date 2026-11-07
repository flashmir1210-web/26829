students = [
    {"name": "김민수", "grade": 1, "club": "밴드부", "attended": True},
    {"name": "이서연", "grade": 2, "club": "코딩부", "attended": True},
    {"name": "박지훈", "grade": 1, "club": "미술부", "attended": False},
    {"name": "최하은", "grade": 2, "club": "밴드부", "attended": True},
    {"name": "정준우", "grade": 1, "club": "코딩부", "attended": False}
]

print("[오늘 출석 명단]")

for student in students:
    if student["attended"]:
        print(student["grade"], "학년", student["name"],
              "(" + student["club"] + ")", "- 출석 완료")

print()
print("[코딩부 명단]")

count = 0

for student in students:
    if student["club"] == "코딩부":
        print("-", student["name"])
        count = count + 1

print("코딩부 총 인원:", count, "명")