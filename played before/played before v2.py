yes = ["yes", "y"]
no = ["no", "n"]
while True:
    played_before = input("have you played before?").strip().lower()
    if played_before in yes:
        print("starting quiz")
        break
    elif played_before in no:
        print("instructions")
        input("press enter to continue")
        print("game starting")
        break
    else:
        print("<error> please enter yes or no")
