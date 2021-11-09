from yesno.yesno_v1 import yesno, yes, no

def user_answers_add(letter,output_yes, output_no):
    while True:
        answer_4_add = input("write what answer {} going to be").lower().format(letter)
        question = "is answer {} \"{}\" " .format(letter,answer_4_add)
        y = yesno(yes, no, question, output_yes, output_no)
        if y == True:
            break


def user_questions(yes, no):
    while True:
        question = "Do you want to add your own questions?"
        output_yes = " "
        output_no = " "
        y = yesno(yes, no, question, output_yes, output_no)
        if y == False:
            break
        else:
            while True:
                question_add = input("write the question you want to add").lower()
                question = "is \"{}\" the question you want to add".format(question_add)
                y = yesno(yes, no, question, output_yes, output_no)
                if y == True:
                    break
                else:
                    answer_1_add = user_answers_add("A",output_yes, output_no)
                    answer_2_add = user_answers_add("B",output_yes, output_no)
                    answer_3_add = user_answers_add("C",output_yes, output_no)
                    answer_4_add = user_answers_add("D",output_yes, output_no)
                    while True:
                        correct_answer_add = input("write what the correct answer is").lower()
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
                    question = "is \"{}\" the correct answer?".format(correct_answer_add)
                    y = yesno(yes, no, question, output_yes, output_no)
                    if y == True:
                        break
                print("question added")
                output_user_questions = [question_add, answer_1_add, answer_2_add, answer_3_add, answer_4_add, correct_answer_add]
                return output_user_questions

    return
