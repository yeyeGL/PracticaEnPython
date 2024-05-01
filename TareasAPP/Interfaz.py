# main.py
import tkinter as tk
from tkinter import messagebox
from Funciones import  guardar_tareas, cargar_tareas,crear_tarea
from Poo import Tarea

class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Tareas")
        self.tareas = cargar_tareas()
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Nombre de la Tarea:").grid(row=0, column=0, sticky="w")
        self.entrada_nombre = tk.Entry(self.root)
        self.entrada_nombre.grid(row=0, column=1)

        tk.Label(self.root, text="Descripcion de la Tarea:").grid(row=1, column=0, sticky="w")
        self.entrada_descripcion = tk.Entry(self.root)  
        self.entrada_descripcion.grid(row=1, column=1)

        self.button_crear = tk.Button(self.root, text="Crear Tarea", command=self.crear_tarea)
        self.button_crear.grid(row=2, column=0, columnspan=2)

        self.panel_tareas = tk.Listbox(self.root, height=10, width=50)
        self.panel_tareas.grid(row=3, column=0, columnspan=2)

        self.boton_guardar = tk.Button(self.root, text="Guardar Tareas", command=self.guardar_tareas)
        self.boton_guardar.grid(row=4, column=0, columnspan=2)

        self.boton_modificar = tk.Button(self.root, text="Modificar Tarea", command=self.modificar_tarea)
        self.boton_modificar.grid(row=5, column=0, columnspan=2)

        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=6, column=0, columnspan=2)

    def crear_tarea(self):
        nombre = self.entrada_nombre.get()
        descripcion = self.entrada_descripcion.get()
        if nombre and descripcion:
            tarea = crear_tarea(nombre, descripcion)
            self.tareas.append(tarea)
            self.panel_tareas.insert(tk.END, str(tarea))
            self.entrada_nombre.delete(0, tk.END)
            self.entrada_descripcion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre y una descripcion")

    def modificar_tarea(self):
        seleccionado = self.panel_tareas.curselection()
        if seleccionado:
            indice = seleccionado[0]
            nueva_nombre = self.entrada_nombre.get()
            nueva_descripcion = self.entrada_descripcion.get()
            if nueva_nombre and nueva_descripcion:
                self.tareas[indice].nombre = nueva_nombre
                self.tareas[indice].descripcion = nueva_descripcion
                self.panel_tareas.delete(indice)
                self.panel_tareas.insert(indice, str(self.tareas[indice]))
                self.entrada_nombre.delete(0, tk.END)
                self.entrada_descripcion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Por favor, ingrese un nombre y una descripcion para modificar")
        else:
            messagebox.showerror("Error", "Por favor, seleccione una tarea para modificar")

    def eliminar_tarea(self):
        seleccionado = self.panel_tareas.curselection()
        if seleccionado:
            indice = seleccionado[0]
            del self.tareas[indice]
            self.panel_tareas.delete(indice)
        else:
            messagebox.showerror("Error", "Por favor, seleccione una tarea para eliminar")

    def guardar_tareas(self):
        guardar_tareas(self.tareas)
        messagebox.showinfo("Exito", "Tareas guardadas exitosamente")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    app.run()
