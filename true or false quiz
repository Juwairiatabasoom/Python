# Question_model
class Question:

    def __init__(self,text,answer):
        self.text=text
        self.ans=answer

#data
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
         " you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament,"
         " you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


#quiz_brain
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


#main 
from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

Question_bank=[]
for que in question_data:
    Que_text=que["text"]
    Que_answer=que["answer"]
    new_que=Question(Que_text,Que_answer)
    Question_bank.append(new_que)

quiz=Quizbrain(Question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("you have completed the quiz")
print(f"your final score was {quiz.score}/{len(Question_bank)}")

