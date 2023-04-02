import random
score = 0
score2 = 0
class Question:
    def __init__(self):
        self.ianswer1 = ""
        self.ianswer2 = ""
        self.ianswer3 = ""
        self.canswer = ""
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.cnum = 0
        self.question = ""

    def set_ianswer1(self, ianswer1):
        self.ianswer1 = ianswer1
    def set_ianswer2(self, ianswer2):
        self.ianswer2 = ianswer2
    def set_ianswer3(self, ianswer3):
        self.ianswer3 = ianswer3
    def set_canswer(self, canswer):
        self.canswer = canswer
    def set_num1(self, num1):
        self.num1 = num1
    def set_num2(self, num2):
        self.num2 = num2
    def set_num3(self, num3):
        self.num3 = num3
    def set_cnum(self, cnum):
        self.cnum = cnum
    def set_question(self, question):
        self.question = question
    def get_ianswer1(self):
        return self.ianswer1
    def get_ianswer2(self):
        return self.ianswer2
    def get_ianswer3(self):
        return self.ianswer3
    def get_canswer(self):
        return self.canswer
    def get_num1(self):
        return self.num1
    def get_num2(self):
        return self.num2
    def get_num3(self):
        return self.num3
    def get_cnum(self):
        return self.cnum

    def PrezQuestion(self):
        count = 1
        start = random.randrange(0, 4)
        print(f"\n{self.question}")
        while count < 5:
            if start == 1:
                words = self.ianswer1
                self.num1 = count
            elif start == 2:
                words = self.ianswer2
                self.num2 = count
            elif start == 3:
                words = self.ianswer3
                self.num3 = count
            elif start == 0:
                words = self.canswer
                self.cnum = count
            start = (start+1)%4
            print(f"{count}: {words}")
            count += 1
    def CheckAnswer(self, score):
        guess = int(input("Enter the number of the answer you think is correct: "))
        if guess == self.cnum:
            score += 1
        return score

question1 = Question()
question1.set_question("Who was the first author to use a 'typemachine' or typewriter when writing a manuscript?")
question1.set_ianswer1("John Griffith Chaney")
question1.set_ianswer2("Sir Arthur Conan Doyle")
question1.set_ianswer3("Raphael Aloysius Lafferty")
question1.set_canswer("Samuel Langhorne Clemens")

question2 = Question()
question2.set_question("What was the first message sent by Morse Code?")
question2.set_ianswer1("Hello")
question2.set_ianswer2("May God bless us all")
question2.set_ianswer3("Testing.. 1..2.. Testing")
question2.set_canswer("What hath God wrought?")

question3 = Question()
question3.set_question("How many legs does a lobster have?")
question3.set_ianswer1("4")
question3.set_ianswer2("6")
question3.set_ianswer3("8")
question3.set_canswer("10")

question4 = Question()
question4.set_question("What is the maximum amount of points you can earn in the arcade version of PacMan?")
question4.set_ianswer1("2,147,483,647")
question4.set_ianswer2("65,535")
question4.set_ianswer3("999,999")
question4.set_canswer("3,333,360")

question5 = Question()
question5.set_question("'Antlophobia' is the fear of: ")
question5.set_ianswer1("Antelope")
question5.set_ianswer2("Antlers")
question5.set_ianswer3("Seeing the future")
question5.set_canswer("Flooding")

question6 = Question()
question6.set_question("Theodore Geisel is:")
question6.set_ianswer1("The holder of the Guinness World Record for fastest speed achieved while skydiving")
question6.set_ianswer2("A stage actor who got his start appearing as an extra in several Monty Python films")
question6.set_ianswer3("The neurologist who operated on Rosemary Kennedy")
question6.set_canswer("A notable author of several books for children and one for adults")

question7 = Question()
question7.set_question("Which Marion isn't real?")
question7.set_ianswer1("Scottish Physicist noted for work in fluid dynamics")
question7.set_ianswer2("National League football player and member of Pro Hall of Fame")
question7.set_ianswer3("John Wayne")
question7.set_canswer("Bartender and onetime underage fling of Henry Jones")

question8 = Question()
question8.set_question("How many floors does the Eiffel Tower Have?")
question8.set_ianswer1("0")
question8.set_ianswer2("4")
question8.set_ianswer3("1")
question8.set_canswer("3")

question9 = Question()
question9.set_question("'wej' means 'three' in what language and 'input' in what other?")
question9.set_ianswer1("Esperanto, Russian")
question9.set_ianswer2("German, Norwegian")
question9.set_ianswer3("Norwegian, Mandarin")
question9.set_canswer("Klingon, Polish")

question10 = Question()
question10.set_question("What English word currently has the most definitions?")
question10.set_ianswer1("get")
question10.set_ianswer2("take")
question10.set_ianswer3("go")
question10.set_canswer("run")

'''
question4 = Question()
question4.set_question("")
question4.set_ianswer1("")
question4.set_ianswer2("")
question4.set_ianswer3("")
question4.set_canswer("")
question4.PrezQuestion()
score = question4.CheckAnswer(score, total)
total += 1
'''

QuestionSet = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
set = random.sample(range(0, 10), 5)
player1 = input("Enter name of first player: ")
player2 = input("Enter name of second player: ")
print(f"\n{player1}'s turn")
for i in set:
    QuestionSet[i].PrezQuestion()
    score = QuestionSet[i].CheckAnswer(score)

print(f"\n{player2}'s turn")
for i in range(0,10):
    if i not in set:
        QuestionSet[i].PrezQuestion()
        score2 = QuestionSet[i].CheckAnswer(score2)

print(f"\n{player1}'s Score: {score}/5")
print(f"{player2}'s Score: {score2}/5")
if score > score2:
    print(f"\n{player1} won!")
elif score == score2:
    print("\nWow! What a tie!")
else:
    print(f"\n{player2} won!")
    