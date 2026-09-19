#dictionary

question1 = {"no": 1, "question": "답을 구하시오", "answer": 1, "score": 5, "isMultipleChoice": False}

questions = [{"no": 2, "question": "답으로 올바른 것을 구하시오", "answer": 3, "score": 5, "isMultipleChoice": True,
              "sample": [1, 2, 3, 4, 5]},

             {"no": 3, "question": "답을 구하시오", "answer": 154, "score": 5, "isMultipleChoice": False},

             {"no": 4, "question": "답을 구하시오", "answer": 523, "score": 5, "isMultipleChoice": False},

             {"no": 5, "question": "답을 구하시오", "answer": 1983, "score": 5, "isMultipleChoice": False},

             {"no": 6, "question": "답을 구하시오", "answer": 2004, "score": 5, "isMultipleChoice": False}]

print(question1["answer"])  # question1의 answer Key의 Value 출력하기

print(questions[1]["question"])