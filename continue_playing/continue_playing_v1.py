from yesno.yesno_v1 import yesno, yes, no


def continue_playing():
    questions = "do you want to continue playing?"
    output_yes = ""
    output_no = ""
    y = yesno(yes, no, question, output_yes, output_no)
    if y == False:
        breakey = true
    return breakey

