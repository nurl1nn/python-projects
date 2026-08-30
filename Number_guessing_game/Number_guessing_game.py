import random
number = random.randint(1,100)
guess= ""
while True:
    try:
        guess=int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if int(guess)<number:
        print("Too low! Try again.")
    elif int(guess)>number:
        print("Too high! Try again.")
    elif int(guess)==number:
         print(f"Congratulations! You guessed the number correctly. Number was: {number}")
         break

        