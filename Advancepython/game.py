import random
user_inputchoice = int(input("Enter choice : Type 0 for Rock , Type 1 for Paper , Type 2 for Scissors"))
if (user_inputchoice >= 3 or user_inputchoice < 0):
    print("The choice is invalid")
else:
    computer_choice = random.randint(0,2)
    print("Computer choose")
    print(computer_choice)
    if (computer_choice == user_inputchoice):
        print("You draw")
    elif (user_inputchoice == 0 and computer_choice == 2):
        print("You win")
    elif (user_inputchoice == 2 and computer_choice == 0):
        print("You lose")        
    elif(computer_choice > user_inputchoice):
        print("You lose")
    elif(user_inputchoice > computer_choice):
        print("You win") 




