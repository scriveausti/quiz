while True:
    played_before = input("have you played before?").strip().lower()
    if played_before == "yes":
        break
    elif played_before == "no":
        print("instructions")
        break
    else:
        print("<error> please enter yes or no")
