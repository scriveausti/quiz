#imports all the sub files
from played_before.played_before_v3 import played_before
from questions.questions_v2 import questions
from score_counter.score_counter_v2 import score_counter
from round_counter.round_counter_v2 import round_counter
from Welcome.welcome_v2 import welcome
from continue_playing.continue_playing_v1 import continue_playing

def main():
    #variabales for the functions
    r=0
    score = 0
    askquestion = [        "question",                 "what is 2003 x 593"]
    answer1 = [         "wrong answer",             "40003453"]
    answer2 = [         "right answer",             "118779"]
    answer3 = [         "wrong answer",             "1187779"]
    answer4 = [         "wrong answer",             "11923422"]
    correct_answer = [  "right answer",             "1187779"]
    yes = ["yes", "y"]
    no = ["no", "n"]
    length = len(askquestion)
    #functions
    welcome()
    played_before()


    while True :
        length = len(askquestion) - 1
        r = round_counter(r)
        win = questions(r, askquestion, answer1, answer2, answer3, answer4, correct_answer, length)
        score = score_counter(win, score)
        breakey = continue_playing(False)
        if breakey == True:
            break

    print("thank you for playing your final score is {} out of {} questions".format(score, r))

main()
