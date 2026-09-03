def add_expense(liste):
     Məbləğ=int(input("Add money: "))
     Kateqoriya=input("Add a category: ")
     Tarix=input("Add a date: ")
     liste.append({"Məbləğ": Məbləğ,"Kateqoriya": Kateqoriya,"Tarix": Tarix})



def show_expenses(liste):
    for x in liste:
        print(f"{x['Məbləğ']}AZN | {x['Kateqoriya']} | {x['Tarix']}")


def total_expenses(liste):
     total=sum(x["Məbləğ"] for x in liste)
     return (total)
liste=[]
daxil=""
while daxil!="N":
    daxil=input("Do you want to add an expense? Y/N: ").upper()
    if daxil=="Y":
        add_expense(liste)
    else:
        break
print("-----All of your expenses-----")
show_expenses(liste)
print(f"Your total expenses is: {total_expenses(liste)}AZN")
        






"""
liste.append({"Məbləğ": int(input("Add money")),"Kateqoriya": input("Add a category"),"Tarix": input("Add a date")})
            umumi=sum([x["Məbləğ"] for x in liste])"""