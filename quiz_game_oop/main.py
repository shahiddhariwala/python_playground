from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_obj = Question(q_text=question["text"], answer=question["answer"])
    question_bank.append(question_obj)

print(repr(question_bank[0]))
