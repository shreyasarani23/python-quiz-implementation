
def select_quiz_option():
    while True:
        try:
            print(
                "Hi Welcome to the quiz\nPlease select your group \n1-> Sports 2->Maths")
            option = int(input("Please enter your choice \n"))
        except ValueError:
            print("Not a number,please try again")
        else:
            if option <= 0 or option > 2:
                print("Invalid value, please try again")
            else:
                return option


def quiz(option):
    score = 0
    if(option == 1):
        ans = input("Q1. Which one is correct team name in NBA? \na. New York Bulls \nb. Los Angeles Kings \nc. Golden State Warriros \nd. Huston Rocket \nplease enter your choice or type the answer \nAnswer:")
        if(ans == "d" or ans == 'Huston Rocket' or ans == 'huston rocket'):
            score += 1
    if(option == 2):
        ans = input(
            "Q1. what is 5 + 7 = ? \na. 10 \nb. 11 \nc. 12 \nd. 13 \nplease enter your choice or type the answer \nAnswer:")
        if(ans == "c" or ans == str(12)):
            score = score+1
        ans = input(
            "\nQ2. what is 12 - 8 = ? \na. 1 \nb. 2 \nc. 3 \nd. 4 \nplease enter your choice or type the answer \nAnswer:")
        if(ans == "d" or ans == str(4)):
            score = score+1
    return score
    
total = quiz(select_quiz_option())
print("Your Total Score is " + str(total))
