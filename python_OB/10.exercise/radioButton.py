import tkinter
from tkinter import ttk
"""En este ejercicio
1 tenéis que crear una lista d RadioButton que 
2 muestre la opción que se ha
seleccionado y
3 que contenga un botón de reinicio para que deje todo como al principio.
4 Al principio no tiene que haber una opción seleccionada.  """

window = tkinter.Tk()  # crea un contenedor

# paso 2 : muestra la opcion seleccionada


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


opcion = tkinter.StringVar()  # le asigno el valor que tenga la variable
opcion.set(None)  # para que no me aparezca ningun seleccionado INSTRUCCION 4
# crea los radio buttons y los muestra con pack() INSTRUCCION 1
tkinter.Radiobutton(window, text="Opción 1", variable=opcion, command=seleccionar,
                    value=1).pack()
tkinter.Radiobutton(window, text="Opción 2", variable=opcion, command=seleccionar,
                    value=2).pack()
tkinter.Radiobutton(window, text="Opción 3", variable=opcion, command=seleccionar,
                    value=3).pack()


# crea la etiqueta donde voy a mostrar la seleccion INSTRUCCION 2
monitor = tkinter.Label(window)
monitor.pack()  # muestra la opcion elegida


def reset():
    opcion.set(None)          # Reiniciamos el seleccionable
    monitor.config(text='')   # Reiniciamos la etiqueta


tkinter.Button(window, text="Reiniciar", command=reset).pack()  # INSTRUCCION 3
window.mainloop()
