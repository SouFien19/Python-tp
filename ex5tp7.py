from tkinter import *

# méthode qui réalise l'action


def action(event):
    # obtenir la valeur du premier champ de saisie
    N = int(entryNumber1.get())
    N2 = 2 * N
    # supprimer la valeur existante sur le deuxième champ
    entryNumber2.delete(0, END)
    # insertion du double N2 = 2 * N
    entryNumber2.insert(0, N2)


# création de la fenêtre principale
fen = Tk()
fen.geometry("430x170")

# Création du label et du premier champ de saisie
lblnumber1 = Label(fen, text="Enter the value of N")
lblnumber1.place(x=50, y=20)
entryNumber1 = Entry(fen)
entryNumber1.place(x=230, y=20)
entryNumber1.bind('<Return>', action)

# Création du deuxième champ de saisie et le label associé
lblnumber2 = Label(fen, text="Here is the double 2*N:")
lblnumber2.place(x=50, y=50)
entryNumber2 = Entry(fen)
entryNumber2.place(x=230, y=50)

fen.mainloop()
