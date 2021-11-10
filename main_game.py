#imports all the sub files
from played_before.played_before_v3 import played_before
from questions.questions_v2 import questions
from score_counter.score_counter_v2 import score_counter
from round_counter.round_counter_v2 import round_counter
from Welcome.welcome_v2 import welcome
from yesno.yesno_v1 import yesno
from user_questions.user_questions_v1 import user_questions
from continue_playing.continue_playing_v1 import continue_playing

def main():
    #variabales for the functions
    r=0
    score = 0
    askquestion = [        "question",                 "question"]
    answer1 = [         "wrong answer",             "wrong answer"]
    answer2 = [         "right answer",             "right answer"]
    answer3 = [         "wrong answer",             "wrong answer"]
    answer4 = [         "wrong answer",             "wrong answer"]
    correct_answer = [  "right answer",             "right answer"]
    yes = ["yes", "y"]
    no = ["no", "n"]
    length = len(askquestion)
    #functions
    welcome()
    played_before()



    while True:
        while True :
            length = len(askquestion)
            r = round_counter(r)
            win = questions(r, askquestion, answer1, answer2, answer3, answer4, correct_answer, length)
            score = score_counter(win, score)
            breakey = continue_playing(False)
            if breakey == True:
                break

        output_user_questions = user_questions(yes,no)
        breakey = continue_playing(True)
        if breakey == True:
            break
        else:
            askquestion = + output_user_questions[0]
            answer1 = + output_user_questions[1]
            answer2 = + output_user_questions[2]
            answer3 = + output_user_questions[3]
            answer4 = + output_user_questions[4]
            correct_answer = + output_user_questions[5]


    main()
