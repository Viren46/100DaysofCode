from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in range(len(question_data)-1):
    obj = Question(question_data[questions]["text"], question_data[questions]["answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
