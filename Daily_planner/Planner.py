to_do=[
    {"Task": "Idman" , "Prioritet": "Yuksek" , "Texmini_vaxt": "1 saat"}
]
tapsiriq=""
prioritet=""
vaxt=""
devam=""
while devam!="O":
    devam = input("What do you want to do: \nAdd task: A  \nExit: O  \nEdit: E  \nSee tasks: S \n").upper()
    if devam=="A":
        tapsiriq=input("Tapsırıq elave et: ")
        prioritet=input("Prioritet teyin et: ")
        vaxt=input("Texmini vaxt teyin et: ")
        yeni_task={"Task": tapsiriq, "Prioritet": prioritet, "Texmini_vaxt": vaxt}
        to_do.append(yeni_task)
    elif devam=="E":
        silinecek = input("Hansı task silinsin: ")
        for task in to_do:
            if task["Task"] == silinecek:
                to_do.remove(task)
                break
    elif devam=="S":
        for task in to_do:
            print(task["Task"],task["Prioritet"],task["Texmini_vaxt"])
print(to_do)