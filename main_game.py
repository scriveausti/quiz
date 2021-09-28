from played_before.played_before_v3 import played_before
from questions.questions_v2 import questions
from score_counter.score_counter_v2 import score_counter
from round_counter.round_counter_v2 import round_counter
from Welcome.welcome_v2 import welcome

def main():
    r=0
    score = 0
    askquestion = [     "what is the best colour?",   "what is the best colour?"]
    answer1 = [         "blue",                       "blue"]
    answer2 = [         "orange",                     "orange"]
    answer3 = [         "red",                        "red"]
    answer4 = [         "green",                      "green"]
    correct_answer = [  "blue",                       "orange"]
    yes = ["yes", "y"]
    no = ["no", "n"]

    welcome()
    played_before()
    while True :
        r = round_counter(r)
        win = questions(r, askquestion, answer1, answer2, answer3, answer4, correct_answer)
        score = score_counter(win, score)

main()
