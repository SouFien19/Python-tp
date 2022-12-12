from tkinter import *

fen = Tk()

fen.geometry("400x200")

fen.title("EXersice 2 Tp7")

b1 = Button(fen, text="Button 1", width=20)

b2 = Button(fen, text="Button 2", width=20)

b3 = Button(fen, text="Button 3", width=20)

b4 = Button(fen, text="Button 4", width=20)

# Run with .pack()

# b1.pack()
# b2.pack()
# b3.pack()
# b4.pack()


# Run with .grid()

b1.grid(column=0, row=0, padx=10, pady=10)
b2.grid(column=1, row=0, padx=10, pady=10)
b3.grid(column=0, row=1, padx=10, pady=10)
b4.grid(column=1, row=1, padx=10, pady=10)

fen.mainloop()
