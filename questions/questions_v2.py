import random

#defines the questions function
def questions(r,askquestion,answer1,answer2,answer3,answer4,correct_answer,length):
    question_num = random.randint(0,length)
    while True:
        #prints the questions and asks the user for the answer
        print("")
        print("question {} {}".format(r, askquestion[question_num]))
        print("a. {}" .format(answer1[question_num]))
        print("b. {}" .format(answer2[question_num]))
        print("c. {}" .format(answer3[question_num]))
        print("d. {}" .format(answer4[question_num]))
        answer = input("A, B, C or D").strip().lower()
        #checks what the user inputed and converts it
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
            print("\n \n \n \n \n \n")
            print("<error> please enter A, B, C or D")
            print("")
    #chscks the answer
    if answer == correct_answer[question_num]:
        win = True
        print("You got this question right \n "
          "Well done ☺")
    else:
        win = False
        print("You got this question wrong \n "
          "the right answer is {}".format(correct_answer[question_num]))
    #returns if the got it right or not
    return win

