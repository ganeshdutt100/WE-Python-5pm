import random

print("Welcome to Rock , paper , Scissors")

options  =  ["rock", "paper", "scissors"]

while True:
    print("Options  :  rock , paper , scissors ,  (Type 'Quit' to exit)")
    user_choice  =  input("Enter your value ")

    if user_choice == "quit":
        print("Game over ") 
        break

    if user_choice not in options:
        print("Wrong spelling , please check ")  
        continue

    computer_choice  =  random.choice(options)
    print('computer choice  :  ' ,  computer_choice)

    if user_choice  == computer_choice:
        print("Tie")

    elif user_choice == "rock" and computer_choice == "scissors":
        print(" user win")

    elif user_choice == "paper" and computer_choice == "rock":
            print(" user win")   
    elif user_choice == "scissors" and computer_choice == "paper":
                print(" user win")    
    else:
          print("Computer Win ")                 


  