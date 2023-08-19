class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_ques = self.question_list[self.question_number]
        self.question_number += 1
        inp = input(f"Q:{self.question_number}.  {current_ques.text} (True/False):  ").capitalize()
        self.check_answer(current_ques.answer, inp)

    def still_has_quest(self):
        length = len(self.question_list)
        return self.question_number < length

    def check_answer(self, correct_ans, inp):
        if correct_ans == inp:
            self.score += 1
            print("You got it Right")

        else:
            print("That's wrong")
        print(f"The correct answer is: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}.")

    def final(self):
        print(f"FINAL SCORE: {self.score}/{self.question_number}")













