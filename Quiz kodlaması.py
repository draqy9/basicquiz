class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer

q1 = Question('en iyi programlama dili hangisidir ?' , ['C#','python','javascript','java'], 'python')
q2 = Question('en populer programlama dili hangisidir ?' , ['C#','python','javascript','java'], 'java')
q3 = Question('en cok kazandiran programlama dili hangisidir ?' , ['C#','python','javascript','java'], 'C#')

questions = [q1,q2,q3]

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return quiz.questions[self.questionIndex]
    def displayQuestion(self): ##Buradaki amac kullanicilara sorulari gostermek
        question = self.getQuestion()
        print(f'Soru {self.questionIndex +1}: {question.text}')

        for q in question.choices:
            print('-'+q)
        answer = input('Cevap: ')
        self.guess(answer)
        self.loadQuestion()
    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print('Score: ', self.score )

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion :
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}' .center(100,' '))


    
quiz = Quiz(questions)
question = quiz.getQuestion()

quiz.displayQuestion()

       






