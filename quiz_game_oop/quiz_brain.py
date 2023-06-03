import html
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Huraah! you are right!")
        else:
            print("Uh oh! incorrect!")
        print(f"Correct answer is : {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = f"Q.{self.question_number} {html.unescape(current_question.text)} (True/False)?: "
        user_input = input(question_text)
        self.check_answer(user_input, current_question.answer)
