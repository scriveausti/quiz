def score_counter(w_l, s):
    if w_l == False:
        print("")
        print("Your score has been decreased by 1")
        s -= 1
        print("your total score is now {}".format(s))
    elif w_l == True:
        print("")
        print("your score has increased by 3")
        s += 3
        print("your total score is now {}".format(s))
    else:
        print("")
        print("<error> something went wrong")
    return s


win = False
score = 0
score = score_counter(win, score)
