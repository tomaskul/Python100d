import data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for item in data.question_data:
    q = Question(text=item["text"], answer=item["answer"])
    questions.append(q)

quiz_brain = QuizBrain(question_list=questions)
quiz_brain.next_question()