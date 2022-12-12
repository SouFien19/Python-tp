from math import gcd
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("350x170")
root.title("PGCD/PPCM")
root.resizable()


def action(event):
    # on récupère la valeur sélectionnée de la liste cobobox
    select = listeCombo.get()

    # récupération de la valeur de m depuis le champ de saisie
    m = int(entry_m.get())
    # récupération de la valeur de n depuis le champ de saisie
    n = int(entry_n.get())

    # plus grand diviseur commun de m et n
    d = gcd(m, n)

    # plus petit multiple commun à m et n
    M = int((m*n)/d)

    if(select == "PGCD"):
        lblResult['text'] = "PGCD  = " + str(d)
    else:
        lblResult['text'] = "PPCM   = " + str(M)


# Création du label et champ de saisie pour l'entier m
lbl_m = Label(root, text="Enter value of m :  ")
entry_m = Entry(root)
lbl_m.place(x=10, y=20)
entry_m.place(x=150, y=20)

# Création du label et champ de saisie pour l'entier n
lbl_n = Label(root, text="Enter value of n :  ")
lbl_n.place(x=10, y=50)
entry_n = Entry(root)
entry_n.place(x=150, y=50)

lblChoose = Label(root, text="Choose function :  ")
lblChoose.place(x=10, y=80)

# Création de la liste combobox pour sélectionner la fonction
listeCombo = ttk.Combobox(root, values=["PGCD", "PPCM"])
listeCombo.place(x=150, y=80, width=165)
listeCombo.bind("<<ComboboxSelected>>", action)

# Création d'un label qui affiche le résultat
lblResult = Label(root, text="Result :  ")
lblResult.place(x=150, y=110)

root.mainloop()
