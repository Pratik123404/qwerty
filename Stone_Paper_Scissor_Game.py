import random

choice = {1:"Stone", 2:"Paper", 3:"Scissor"}

Value = random.choice(list(choice.keys()))

computer = choice[Value]

Me = (input("Enter your choice: "))
print(f"You entered: {Me}")

print(f"Computer entered: {computer}")

if(Me==computer):
    print("It's a draw")
else:
    if(Me=="Stone" and computer=="Paper"):
        print("You lose, "+"Computer won")
    elif(Me=="Stone" and computer=="Scissor"):
        print("You win, "+"Computer lose")
    elif(Me=="Paper" and computer=="Stone"):
        print("You win, "+"Computer lose")
    elif(Me=="Paper" and computer=="Scissor"):
        print("You lose, "+"Computer won")
    elif(Me=="Scissor" and computer=="Stone"):
        print("You lose, "+"Computer won")
    elif(Me=="Scissor" and computer=="Paper"):
        print("You win, "+"Computer lose")
    elif(Me=="Scissor" and computer=="Stone"):
        print("You lose, "+"Computer won")
    else:
        print("Invalid option")


