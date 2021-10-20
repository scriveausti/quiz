yes = ["yes", "y"]
no = ["no", "n"]

#defines the played before function
def played_before():
    while True:
        #asks the user if they have played before
        played_before = input("have you played_before?").strip().lower()
        #checks if yes or no
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
