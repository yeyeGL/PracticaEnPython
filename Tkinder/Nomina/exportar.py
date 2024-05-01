from tkinter import messagebox

def exportar_resultados(resultados):
    with open("resultados.txt", "w") as file:
        file.write(resultados)
    messagebox.showinfo("Exitoso", "Exportado a resultados.txt")