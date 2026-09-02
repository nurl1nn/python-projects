daxil=""
while daxil!="E":
    daxil=input("What do you want to do:  \n1.Add: Write A \n2.Divide: Write D \n3.Subtract: Write S \n4.Multiply: Write M  \n5.Exit: Write E \nChosen: ").upper()
    if daxil=="E":
        break
    try:
        eded=int(input("Input a number: "))
        eded2=int(input("Input another number: "))
    except ValueError:
        print("You should add a number")
        continue
    if daxil=="A":
        print("Result:", eded+eded2 )
    elif daxil=="D":
        try:
            print("Result:", eded/eded2)
        except ZeroDivisionError:
            print("You can't divide it to zero")
    elif daxil=="S":
        print("Result:",eded-eded2)
    elif daxil=="M":
        print("Result:", eded*eded2)
    else:
       print("That is not defined")