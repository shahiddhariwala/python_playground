class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return len(self.question_list) >= self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = f"Q.{self.question_number} {current_question.text} (True/False)?: "
        user_input = input(question_text)
        if user_input == current_question.answer:
            print("Correct answer!")
        else:
            print("Incorrect answer!")
