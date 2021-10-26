from yesno.yesno_v1 import yesno, yes, no


def user_questions(yes, no):
    while True:
        question = "Do you want to add your own questions?"
        output_yes = ""
        output_no = ""
        y = yesno(yes, no, question, output_yes, output_no)
        if y == False:
            break
        else:
            while True:
                question_add = input("write the question you want to add").lower
                question = "is \"{}\" the question you want to add".format(question_add)
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
            while True:
                answer_1_add = input("write what answer A going to be").lower
                question = "is \"{}\" answer A" .format(answer_1_add)
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
            while True:
                answer_2_add = input("write what answer B going to be").lower
                question = "is \"{}\" answer B" .format(answer_2_add)
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
            while True:
                answer_3_add = input("write what answer A going to be").lower
                question = "is \"{}\" answer B" .format(answer_3_add)
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
            while True:
                answer_4_add = input("write what answer A going to be").lower
                question = "is \"{}\" answer B" .format(answer_4_add)
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
            while True:
                while True:
                    correct_answer_add = input("write what the correct answer is").lower
                    if correct_answer_add == answer_1_add or correct_answer_add == answer_2_add or correct_answer_add == answer_3_add or correct_answer_add == answer_4_add:
                        break
                    elif correct_answer_add == "a":
                        correct_answer_add = answer_1_add
                        break
                    elif correct_answer_add == "b":
                        correct_answer_add = answer_2_add
                        break
                    elif correct_answer_add == "c":
                        correct_answer_add = answer_3_add
                        break
                    elif correct_answer_add == "d":
                        correct_answer_add = answer_4_add
                        break
                    else:
                        print("<error> please enter what the correct answer is")
                question = "is \"{}\" the correct answer?"
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
            output_user_questions = [question_add, answer_1_add, answer_2_add, answer_3_add, answer_4_add, correct_answer_add]
    return output_user_questions


user_questions(yes, no)