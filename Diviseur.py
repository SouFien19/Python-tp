from tkinter import *

# méthode qui réalise l'action


def action():

    # obtenir la valeur de N depuis le champ de saisie
    N = int(entryNumber1.get())
    lblDivisors['text'] = 'The  divisors  of  N    :    '

    # parcourir les eniers de 1 à N et rechercher les diviseurs de N
    for i in range(1, N + 1):
        if (N % i == 0):
            lblDivisors['text'] = lblDivisors['text'] + "   " + str(i) + "   "


# Creation de la fenêtre principale
fen = Tk()
fen.geometry("400x175")

# champ de saisie pour l'entier N
lblnumber1 = Label(fen, text="Enter the value of N")
lblnumber1.place(x=10, y=20)
entryNumber1 = Entry(fen)
entryNumber1.place(x=200, y=20)

# Label qui affiche le résultat
lblDivisors = Label(fen, text="The divisors of N : ")
lblDivisors.place(x=10, y=50)

# bouton de validation
Validate = Button(fen, text="Validate", width=20, command=action)
Validate.place(x=200, y=90)

fen.mainloop()
