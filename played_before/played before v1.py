while True:
    played_before = input("have you played_before?").strip().lower()
    if played_before == "yes" or played_before == "y":
        print("starting quiz")
        break
    elif played_before == "no" or played_before == "n":
        print("instructions")
        input("press enter to continue")
        print("game starting")
        break
    else:
        print("<error> please enter yes or no")
