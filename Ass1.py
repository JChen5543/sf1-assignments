print("This program will calculate your final grade of the semester, please enter what you are asked to.")

nbprob = int(input("How many Lab Programming Problems have you completed?"))
nbquiz = int(input("How many quizzes have you completed?"))

Ass1 = float(input("What grade did you get on the first assignment?")) 
Ass2 = float(input("What grade did you get on the second assignment?"))
Ass3 = float(input("What grade did you get on the third assignmemt?"))
Ass4 = float(input("What grade did you get on the fourth assignment?"))

Mid1 = float(input("What grade did you get on the first Midterm and it's preparation?"))
Mid2 = float(input("What grade did you get on the second Midterm and it's preparation?"))

Final = float(input("What grade did you get on the final?"))

TotalAss = (Ass1 * (4/100) + Ass2 * (4/100) + Ass3 * (4/100) + Ass4 * (4/100))
TotalMid = (Mid1 * (15.5/100) + Mid2 * (15.5/100))
FinalExam = Final * (18/100)


if nbprob > 6:
    prob = (6 * (10/3))
if nbprob <= 6 and nbprob >= 0:
    prob = (nbprob * (10/3))
if nbprob < 0:
    prob = 0

if nbquiz > 6:
    quiz = (6 * (2.5))
if nbquiz <= 6 and nbquiz >= 0:
    quiz = (nbquiz * (2.5))
if nbquiz < 0:
    quiz = 0 

Total = round((TotalAss + TotalMid + quiz + prob + FinalExam), 2)
print("Your grade is:", " ", Total)
