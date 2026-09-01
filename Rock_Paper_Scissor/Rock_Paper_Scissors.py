import random
liste = ["Rock","Paper","Scissor"]
again=""
while again !="n":
    bot =random.choice(["Rock","Paper","Scissor"])
    chosen=input("Choose one of these: Rock , Paper, Scissor\n").capitalize()
    if chosen not in liste:
        print("Invalid input")
        continue
    if chosen==bot:
        print(f"Bot choose:{bot}")
        print(f"You choose:{chosen}")
        print("Draw")
        again= input("Do you want play again? y/n: ")
    elif (bot=="Rock" and chosen=="Paper") or (bot=="Paper" and chosen=="Scissor") or (bot=="Scissor" and chosen=="Rock"):
        print(f"Bot choose: {bot}")
        print(f"You choose:{chosen}")
        print("You win!")
        again= input("Do you want play again? y/n: ")
    else:
        print(f"Bot choose:{bot}")
        print(f"You choose:{chosen}")
        print("You lose!")
        again= input("Do you want play again? y/n: ")
print("Thanks for playing")