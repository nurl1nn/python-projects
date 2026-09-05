import random
import string
upper_l=string.ascii_uppercase
lower_l=string.ascii_lowercase
digits=string.digits
simvol=string.punctuation
password=[]
cavab=""
choice=""
say=""
while True:
    cavab=input("Do you want to generate a password? Y/N: ").upper()
    if cavab=="Y":
        choice=input("What do you want in your password? \nUpper case: U \nLower case: L \nDigits: D \nPunctuation: P: \n").upper()
        say=int(input("Input count for it: "))
        if choice=="U":
            for i in range(say):
                password.append(random.choice(upper_l))
        elif choice=="L":
            for i in range(say):
                password.append(random.choice(lower_l))
        elif choice=="D":
            for i in range(say):
                password.append(random.choice(digits))
        elif choice=="P":
            for i in range(say):
                password.append(random.choice(simvol))
    elif cavab=="N":
        break
random.shuffle(password)  
print(f"This is your password: {''.join(password)}")  