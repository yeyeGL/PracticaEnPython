
from tkinter import Button, Entry, Label, messagebox
import tkinter as tk
from InterfazTrabajador import Application


def ventana_Principal():

    ventana.destroy()
    app = Application()
    app.mainloop()

ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Interfaz de inicio de sesion")

def salir():
    ventana.quit()
    ventana.destroy()
    
def verificar_Usuario_Contraseña():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    if usuario == "u" and contraseña == "123":
        mensaje1 = messagebox.showinfo("Exitoso", "Usuario y contraseña correcta")
        ventana_Principal()
    else:
        mensaje1 = messagebox.showerror("Error", "Inicio de sesion no valida")

usuario_label = Label(ventana, text="Usuario")
usuario_label.pack()

usuario_entry = Entry(ventana)
usuario_entry.pack()

contraseña_label = Label(ventana, text="Contraseña")
contraseña_label.pack()

contraseña_entry = Entry(ventana)
contraseña_entry.pack()

boton_login = Button(ventana, text="Iniciar sesion", command=verificar_Usuario_Contraseña)
boton_login.pack()

ventana.mainloop()
