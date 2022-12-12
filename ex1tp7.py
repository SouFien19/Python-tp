from tkinter import *

fen = Tk()

fen.geometry("400x200")

fen.title("EXersice 1 Tp7")

b1 = Button(fen, text="Button 1")

b2 = Button(fen, text="Button 2")

b3 = Button(fen, text="Button 3")

b4 = Button(fen, text="Button 4")

# Run with .pack()

# b1.pack()
# b2.pack()
# b3.pack()
# b4.pack()


# Run with .grid()

b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=0, row=1)
b4.grid(column=1, row=1)

fen.mainloop()
