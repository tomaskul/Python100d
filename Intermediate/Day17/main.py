import data
from question_model import Question

questions = []

for item in data.question_data:
    q = Question(text=item["text"], answer=item["answer"])
    questions.append(q)
    print(f"Q: {q.text}\tA: {q.answer}")
