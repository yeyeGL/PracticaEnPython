import tkinter as tk
from tkinter import messagebox, Listbox
import psycopg2
import json

class InterfazTrabajador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trabajador")
        self.geometry("600x400")

        
        self.tareas_label = tk.Label(self, text="Tareas:")
        self.tareas_label.pack(pady=10)

        
        self.tareas_listbox = Listbox(self, height=10, width=50)
        self.tareas_listbox.pack(pady=10)

        self.marcar_completado_button = tk.Button(self, text="Marcar como Completado", command=self.marcar_completado)
        self.marcar_completado_button.pack(pady=10)

    
        self.exportar_tareas_button = tk.Button(self, text="Exportar Tareas", command=self.exportar_tareas)
        self.exportar_tareas_button.pack(pady=10)


        self.cargar_tareas()

    def cargar_tareas(self):
        try:
            conn = psycopg2.connect(dbname="db-tareas", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, descripcion, completada FROM tareas")
            tareas = cursor.fetchall()
            cursor.close()
            conn.close()

         
            self.tareas_listbox.delete(0, tk.END) 
            for tarea in tareas:
                self.tareas_listbox.insert(tk.END, f"{tarea[0]} - {tarea[1]}")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al cargar las tareas paila: {e}")

    def marcar_completado(self):
        try:
            conn = psycopg2.connect(dbname="db-tareas", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            
           
            nombre_tarea = "actualizar"  
            
            cursor.execute("UPDATE tareas SET completada = TRUE WHERE nombre = %s", (nombre_tarea,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Yuhuuu", "Tarea marcada como completada")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al marcar la tarea como completada: {e}")

    def exportar_tareas(self):
        try:
            conn = psycopg2.connect(dbname="db-tareas", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, descripcion, completada FROM tareas")
            tareas = cursor.fetchall()
            cursor.close()
            conn.close()

            tareas_json = [{"nombre": tarea[0], "descripcion": tarea[1], "completada": tarea[2]} for tarea in tareas]
            with open('tareas.json', 'w') as file:
                json.dump(tareas_json, file)
            messagebox.showinfo("yeah", "Tareas exportadas exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al exportar las tareas: {e}")

if __name__ == "__main__":
    app = InterfazTrabajador()
    app.mainloop()
