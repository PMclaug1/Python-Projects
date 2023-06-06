from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = [
    
]

for i in question_data:
    new_q = Question(i["text"], i["answer"])
    question_bank.append(new_q)

quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Your final score is {quiz.score}/{quiz.question_number}")