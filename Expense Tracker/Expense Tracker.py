import csv
def load_from_csv():
    liste=[]
    try:
          with open("file.csv","r",encoding="utf-8") as f:
               reader=csv.DictReader(f)
               for row in reader:
                    row["Məbləğ"] = int(row["Məbləğ"])
                    liste.append(row)
    except FileNotFoundError:
        print("No previous expenses found.")
    return liste      
def add_expense(liste):
     try:
          Məbləğ=int(input("Add money: "))
     except ValueError:
          print("You can add number")
          return
     Kateqoriya=input("Add a category: ")
     Tarix=input("Add a date: ")
     liste.append({"Məbləğ": Məbləğ,"Kateqoriya": Kateqoriya,"Tarix": Tarix})
def show_expenses(liste):
    for x in liste:
        print(f"{x['Məbləğ']}AZN | {x['Kateqoriya']} | {x['Tarix']}")
def total_expenses(liste):
     total=sum(x["Məbləğ"] for x in liste)
     return (total)
def save_to_csv(liste):
     with open("file.csv", "w",encoding="utf-8") as f:
          yazici=csv.DictWriter(f, fieldnames=["Məbləğ" , "Kateqoriya", "Tarix"])
          yazici.writeheader()
          for d in liste:
            yazici.writerow(d)
liste=load_from_csv()
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
save_to_csv(liste)
