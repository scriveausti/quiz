yes = ["yes", "y"]
no = ["no", "n"]

#defines the yes no function
def yesno(yes, no, question, output_yes, output_no):
    while True:
        answer = input("{}".format(question)).strip().lower()
        if answer in yes:
            print(output_yes)
            y = True
            return y
        elif answer in no:
            print(output_no)
            y = False
            return y
        else:
            print("<error> please enter yes or no")
