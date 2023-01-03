"""En este segundo ejercicio, tendréis que
crear una interfaz sencilla la cual debe de
contener una lista de elementos seleccionables,
también debe de tener un label con el texto que queráis.  """

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


window = tk.Tk()
frame = tk.Frame(window)
lista = ["Arroz", "Leche", "Huevo", "Azucar", "Agua"]
var = tk.Variable(value=lista)
listbox = tk.Listbox(frame, height=5, listvariable=var, selectmode=tk.EXTENDED)
listbox.pack(padx=30, pady=30)
action = tk.Label(frame, text="Compras", bg="green", fg="white")
action.pack(padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)
#
window.mainloop()
