import tkinter as tk
from tkinter import messagebox
from ad import InterfazAdmin
from tra import InterfazTrabajador

def login():
    aliasl = aliasl.get()
    clave = clave.get()
    tipousuario = tipousuario.get()


    if tipousuario == "admin" and aliasl == "admin" and clave == "123":
        messagebox.showinfo("Bien entre", "Bienvenido!")
       
        InterfazAdmin()
    elif tipousuario == "worker" and aliasl == "worker" and clave == "123":
        messagebox.showinfo("bien entre", "Bienvenido!")
        
        InterfazTrabajador()
    else:
        messagebox.showerror("3 a 0", "Incorrecto brother")

    def admin_interface():
        app = InterfazAdmin()  
        app.mainloop()

    def worker_interface():
        app = InterfazTrabajador() 
        app.mainloop()


root = tk.Tk()
root.title("LOGIN")

username_label = tk.Label(root, text="Usuario:")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)


password_label = tk.Label(root, text="Clave:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Ingresar", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

user_type_label = tk.Label(root, text="Tipo de usuario:")
user_type_label.grid(row=3, column=0, padx=10, pady=10)

user_type_var = tk.StringVar(root)
user_type_var.set("admin")  # default value
user_type_option = tk.OptionMenu(root, user_type_var, "Jefe", "Trabajador")
user_type_option.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
