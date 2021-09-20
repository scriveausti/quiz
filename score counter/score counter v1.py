score = 0
win = False
if win == False:
    print("")
    print("Your score has been decreased by 1")
    score -= 1
    print("your total score is now {}".format(score))
elif win == True:
    print("")
    print("your score has increased by 3")
    score += 3
    print("your total score is now {}".format(score))
else:
    print("")
    print("<error> something went wrong")
