import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import psycopg2
import json

class InterfazAdmin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jefe")
        self.geometry("800x600")

        self.nombrel = tk.Label(self, text="Nombre de la tarea:")
        self.nombrel.grid(row=0, column=0, padx=10, pady=10)
        self.nombre= tk.Entry(self)
        self.nombre.grid(row=0, column=1, padx=10, pady=10)

        self.descripcionl = tk.Label(self, text="Descripción de la tarea:")
        self.descripcionl.grid(row=1, column=0, padx=10, pady=10)
        self.descripcion = tk.Entry(self)
        self.descripcion.grid(row=1, column=1, padx=10, pady=10)

       
        self.creartareaboton = tk.Button(self, text="Crear Tarea", command=self.crear_tarea)
        self.creartareaboton.grid(row=2, column=0, columnspan=2, pady=10)

   
        self.vertareasboton = tk.Button(self, text="Ver Tareas", command=self.ver_tareas)
        self.vertareasboton.grid(row=3, column=0, columnspan=2, pady=10)

 
        self.eliminartareaboton = tk.Button(self, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminartareaboton.grid(row=4, column=0, columnspan=2, pady=10)

    def crear_tarea(self):
        try:
            conn = psycopg2.connect(dbname="db-tareas", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tareas (nombre, descripcion) VALUES (%s, %s)", (self.nombre.get(), self.descripcion.get()))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Yeah", "Tarea creada exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al crear la tarea: {e}")

    def ver_tareas(self):
        try:
            conn = psycopg2.connect(dbname="db-tareas", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tareas")
            tareas = cursor.fetchall()
            cursor.close()
            conn.close()

            self.tareaslista = ttk.Treeview(self, columns=("Nombre", "Descripcion"), show="headings")
            self.tareaslista.heading("Nombre", text="Nombre")
            self.tareaslista.heading("Descripcion", text="Descripcion")
            self.tareaslista.grid(row=5, column=0, columnspan=2, pady=10)

            for tarea in tareas:
                self.tareaslista.insert("", "end", values=tarea)

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al ver las tareas: {e}")

    def eliminar_tarea(self):
        try:
            
            seleccionItemes = self.tareaslista.selection()
            if not seleccionItemes:
                messagebox.showerror("Error", "Debe seleccionar una tarea para eliminar")
                return

           
            seleccionItemes = seleccionItemes[0]

            nombre_tarea = self.tareaslista.item(seleccionItemes, "values")[0]

            conn = psycopg2.connect(dbname="db-tareas", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tareas WHERE nombre = %s", (nombre_tarea,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Yuhuu", "Tarea eliminada exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al eliminar la tarea: {e}")



if __name__ == "__main__":
    app = InterfazAdmin()
    app.mainloop()
