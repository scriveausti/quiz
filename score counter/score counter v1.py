score = 0
win = 0
if win == True:
    print("")
    print("Your score has been decreased by 1")
    score -= 1
    print("your total score is now {}".format(score))
elif win == False:
    print("")
    print("your score has increased by 3")
    score += 3
    print("your total score is now {}".format(score))
else:
    print("")
    print("<error> something went wrong")
