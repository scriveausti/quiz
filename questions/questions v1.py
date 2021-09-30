r =1

import random

question = [        "question",                 "question"]
answer1 = [         "wrong answer",             "wrong answer"]
answer2 = [         "right answer",             "right answer"]
answer3 = [         "wrong answer",             "wrong answer"]
answer4 = [         "wrong answer",             "wrong answer"]
correct_answer = [  "right answer",             "right answer"]


question_num = random.randint(0,1)
while True:
    print("")
    print("question {} {}".format(r, question[question_num]))
    print("a. {}" .format(answer1[question_num]))
    print("b. {}" .format(answer2[question_num]))
    print("c. {}" .format(answer3[question_num]))
    print("d. {}" .format(answer4[question_num]))
    answer = input("A, B, C or D").strip().lower()
    if answer == "a" :
        answer = answer1[question_num]
        break
    elif answer == "b" :
        answer = answer2[question_num]
        break
    elif answer == "c" :
        answer = answer3[question_num]
        break
    elif answer == "d" :
        answer = answer4[question_num]
        break
    else:
        print("")
        print("<error> please enter A, B, C or D")

if answer == correct_answer[question_num]:
    win = True
    print("You got this question right \n "
          "Well done ☺")
else:
    win = False
    print("You got this question wrong \n "
          "the right answer is {}".format(correct_answer[question_num]))
