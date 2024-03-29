from question_model import Question
from data import question_data, get_random_question_data
from quiz_brain import QuizBrain
question_bank = []
for question in get_random_question_data():
    question_obj = Question(q_text=question["text"], answer=question["answer"])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

user_score = quiz.score
print(f"You've completed the quiz!\nYour final score is {user_score}/{len(quiz.question_list)}")
