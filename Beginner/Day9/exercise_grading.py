student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

scoring_criteria = {
    "Outstanding": range(91, 101),
    "Exceeds Expectations": range(81, 91),
    "Acceptable": range(71, 81),
}

student_grades = {}

def grade_students():
    for student in student_scores:
        score = student_scores[student]

        criteria_met = False
        for criteria in scoring_criteria:
            score_range = scoring_criteria[criteria]
            if score in score_range:
                criteria_met = True
                student_grades[student] = criteria
        
        if not criteria_met:
            student_grades[student] = "Fail"


grade_students()
print(student_grades)