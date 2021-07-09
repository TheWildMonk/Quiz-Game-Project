class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.question_list = questions_list

    # def next_question(self):
    #     for question in self.question_list:
    #         question = self.question_list[self.question_number]
    #         input(f"Q{self.question_number}. {question.text}")
    #         self.question_number += 1
