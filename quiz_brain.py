
class QuizBrain:

    def __init__(self, q_list):
        self.ques_number = 0
        self.ques_list = q_list
        self.score = 0

    def still_has_ques(self):
        length = len(self.ques_list)
        return self.ques_number < length

    def next_ques(self):
        current_ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        user_answer = input(f"Q.{self.ques_number}: {current_ques.text} (True/False): ")
        self.check_answer(user_answer, current_ques.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("This is wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.ques_number}")
        print("\n")



