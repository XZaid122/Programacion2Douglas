import tkinter as tk
from tkinter import messagebox



ventana = tk.Tk()
ventana.title("Login")


frame = tk.Frame(ventana, width=300, height=800, relief="raised", bd=1)
frame.grid(row=0, column=0, pady=0)

ventana.geometry("600x500")
ventana.resizable(False, False)

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "contraseña":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Nombre de usuario o contraseña incorrectos")

frame = tk.Frame(ventana, bg="skyblue")
frame.place(relx=0.5, rely=0.5, anchor="sw")

label_username = tk.Label(frame, text="Nombre de usuario:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(frame, text="Contraseña:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
