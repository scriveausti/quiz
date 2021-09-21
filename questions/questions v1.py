r =1

import random

question = [        "what is the best colour?",   "what is the best colour?"]
answer1 = [         "blue",                       "blue"]
answer2 = [         "orange",                     "orange"]
answer3 = [         "red",                        "red"]
answer4 = [         "green",                      "green"]
correct_answer = [  "blue",                       "orange"]


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

if answer == correct_answer:
    win = True
else:
    win = False