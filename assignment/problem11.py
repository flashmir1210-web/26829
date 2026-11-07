movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]

print("[평점 8.5 이상 영화]")

total_views = 0
max_views = 0
max_title = ""

for movie in movies:
    if movie["rating"] >= 8.5:
        print(movie["title"])

    if movie["genre"] == "애니메이션":
        total_views = total_views + movie["views"]

    if movie["views"] > max_views:
        max_views = movie["views"]
        max_title = movie["title"]

print("애니메이션 총 조회수:", total_views, "회")
print("최다 조회수 영화:", max_title, "(", max_views, "회)")