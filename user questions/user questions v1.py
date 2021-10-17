def user_questions(askquestion, answer1, answer2, answer3, answer4, correct_answer, yes, no):
    while True:
        yesno = input("Do you want to add your own questions?")
        if yesno in yes:
            question = input("What is the question you want tot add?")
            confirm
        elif yesno in no:
            break
        else:
            print("<error> please enter yes or no")
