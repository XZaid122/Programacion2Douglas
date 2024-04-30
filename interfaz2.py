import tkinter as tk 
from tkinter import messagebox

def registrar():
    mensaje = f"Nombre: {Cnombre.get()}\nApellido: {Capellido.get()}\nEdad: {Cedad.get()}\nDirección: {Cdireccion.get()}\nSexo: {elige_genero.get()}\nTeléfono: {Ctelefono.get()}\nCiudad: {selecciona_ciudad.get()}"
    messagebox.showinfo("Datos registrados", mensaje)

ventana=tk.Tk()
ventana.title("Tecnar App")
ventana.geometry("800x600")
ventana.resizable(True,True)
ventana.config(bg="grey")

Lnombre=tk.Label(ventana,text="Nombre:" )
Lnombre.grid(row = 0, column = 18, pady = 4)
Cnombre=tk.Entry(ventana, width=30)
Cnombre.grid(row = 1, column = 18, pady = 4)

Lapellido=tk.Label(ventana,text="Apellido:" )
Lapellido.grid(row = 3, column = 18, pady = 4)
Capellido=tk.Entry(ventana, width=30)
Capellido.grid(row = 4, column = 18, pady = 4)

Ledad=tk.Label(ventana,text="Edad:" )
Ledad.grid(row = 5, column = 18, pady = 4)
Cedad=tk.Entry(ventana, width=30)
Cedad.grid(row = 6, column = 18, pady = 4)

Ldireccion=tk.Label(ventana,text="Direccion:")
Ldireccion.grid(row = 7, column= 18, pady= 4)
Cdireccion=tk.Entry(ventana, width=30)
Cdireccion.grid(row = 8, column = 18, pady = 4)

Lsexo=tk.Label(ventana,text="Sexo:")
Lsexo.grid(row = 9, column= 18, pady= 4)
elige_genero = tk.StringVar()

tk.Radiobutton(ventana, text="Masculino", variable=elige_genero, value="Masculino").grid(row=10, column=18, pady=4)
tk.Radiobutton(ventana, text="Femenino", variable=elige_genero, value="Femenino").grid(row=11, column=18, pady=4)

Ltelefono=tk.Label(ventana,text="Telefono:")
Ltelefono.grid(row=12, column=18, pady=4)
Ctelefono=tk.Entry(ventana, width=30)
Ctelefono.grid(row=13, column=18, pady=4)

Lciudad=tk.Label(ventana,text="Ciudad:")
Lciudad.grid(row=14, column=18, pady=4)

selecciona_ciudad = tk.StringVar()

ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]

ciudad_lista = tk.Listbox(ventana, height=5)
ciudad_lista.grid(row=15, column=18, pady=4)

for ciudad in ciudades:
    ciudad_lista.insert(tk.END, ciudad)

def on_select(event):
    selecciona_ciudad.set(event.widget.get(event.widget.curselection()))

ciudad_lista.bind('<<ListboxSelect>>', on_select)

Registrar = tk.Button(ventana, text="Registrar", command=registrar)
Registrar.grid(row = 17, column = 1, pady = 4)

ventana.mainloop()