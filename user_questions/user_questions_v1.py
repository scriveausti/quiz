from yesno.yesno_v1 import yesno


def user_questions(askquestion, answer1, answer2, answer3, answer4, correct_answer, yes, no):
    while True:
        question = "Do you want to add your own questions?"
        output_yes = ""
        output_no = ""
        y = yesno(yes, no, question, output_yes, output_no)
        if y == False:
            break
        else:
            question = "What is the question you want tot add?"
            output_yes = ""
            output_no = ""
            y = yesno(yes, no, question, output_yes, output_no)

