# functions.py
import json
from Poo import Tarea

def crear_tarea(nombre, descripcion):
    return Tarea(nombre, descripcion)

def guardar_tareas(tareas):
    with open('tareas.json', 'w') as file:
        json.dump([tarea.__dict__ for tarea in tareas], file)



def cargar_tareas():
    try:
        with open('tareas.json', 'r') as file:
            tareas_data = json.load(file)
            return [Tarea(**tarea_data) for tarea_data in tareas_data]
    except FileNotFoundError:
        return []
        
