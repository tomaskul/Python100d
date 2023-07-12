class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def next_question(self):
        if self.question_number == len(self.question_list):
            self.question_number = 0
        
        current_q = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)?:\t")
        if self.check_answer(user_answer=user_answer, correct_answer=current_q.answer):
            print("You're right!")
            self.score += 1
        else:
            print(f"You're wrong, correct answer was {current_q.answer}, your final score: {self.score}")
            self.question_number = len(self.question_list)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)