yes = ["yes", "y"]
no = ["no", "n"]

#defines the played before function
def played_before():
    while True:
        #asks the user if they have played before
        played_before = input("have you played before?").strip().lower()
        #checks if yes or no
        if played_before in yes:
            print("starting quiz")
            break
        elif played_before in no:
            print("instructions\n"
                  "\n"
                  "there will be a questions displaed\n"
                  "and you will need to write a,b,c or d and press enter")
            input("press enter to continue")
            print("game starting")
            break
        else:
            print("<error> please enter yes or no")
