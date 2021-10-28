from yesno.yesno_v1 import yesno, yes, no


def continue_playing(play_again):
    if play_again == False:
        questions = "do you want to continue playing?"
        output_yes = ""
        output_no = ""
        y = yesno(yes, no, questions, output_yes, output_no)
        if y == False:
            breakey = True
        return breakey
    elif play_again == True:
        questions = "do you want to play again ?"
        output_yes = ""
        output_no = ""
        y = yesno(yes, no, questions, output_yes, output_no)
        if y == False:
            breakey = True
        return breakey

