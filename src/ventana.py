import tkinter as tk
 
ventana = tk.Tk()
ventana.title("mi primera ventana")

label = tk.Label(ventana, text="¡hola, mundo!")
label.pack()

boton = tk.Button(ventana, text="haz clic aqui")
boton.pack()

import tkinter as tk 
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡boton presionado!")

label = tk.Label(ventana, text="presiona el boton para ver un mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text="haz clic aqui", command=mostrar_mensaje)
boton.pack(pady=10)



ventana.mainloop()