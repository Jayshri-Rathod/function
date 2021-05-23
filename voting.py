age=int(input("enter age"))
def eligible_for_vote():
    if age<18:
        print("not eligible")
    else:
        print("you are eligible")
eligible_for_vote()