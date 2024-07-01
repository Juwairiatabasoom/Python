class Quizbrain:

    def __init__(self, question_list):
        self.que_no = 0
        self.score=0
        self.que_list = question_list

    def next_question(self):
        cur_ques = self.que_list[self.que_no]
        self.que_no+=1
        ans_typed=input(f" Q.{self.que_no}:{cur_ques.text}(True/False):")
        self.check_answer(ans_typed,cur_ques.ans)

    def still_has_questions(self):
        return self.que_no<len(self.que_list)

    def check_answer(self,ans_typed,correct_answer):
         if ans_typed.lower() == correct_answer.lower():
             print("Yay!correct")
             self.score+=1
         else:
            print("you got it wrong")
         print(f"the correct answer was {correct_answer}")
         print(f"Your current score is {self.score}/{self.que_no}")
         print("\n")





