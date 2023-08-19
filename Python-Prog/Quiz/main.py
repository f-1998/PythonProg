from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for i in range(len(question_data)):
    q = question_data[i]["text"]
    a = question_data[i]["answer"]
    question_bank.append(Question(q, a))


quiz = QuizBrain(question_bank)

while quiz.still_has_quest():
    quiz.next_question()

print("\nYou have completed the challenge.")
quiz.final()








