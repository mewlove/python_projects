# (control + '/' for comments)

def user_choice():
    choice = "WRONG"
    while not choice.isdigit() or int(choice)>10 or int(choice)<0:
        choice = input("Please input a digit (0-10): ")
    return int(choice)
#user_choice()