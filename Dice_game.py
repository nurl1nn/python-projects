import random
daxil = " "
while True:
    daxil = input("Roll the dice? Y/N: ").upper()
    if daxil=="Y":
       print(f"({random.randint(1,6)},{random.randint(1,6)})")
    elif daxil=="N":
        break
    else:
        print("Invalid choice")
print("Thanks for playing")