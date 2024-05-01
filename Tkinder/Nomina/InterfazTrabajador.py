import tkinter as tk
from Funciones import Trabajador
from exportar import exportar_resultados

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Trabajador Application")
        self.geometry("400x400")

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        archivo_menu.add_command(label="Salir", command=self.salir)

        acerca_de_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Acerca de", menu=acerca_de_menu)

        acerca_de_menu.add_command(label="Acerca del proyecto", command=self.acerca_de_proyecto)
        acerca_de_menu.add_command(label="Nombre de los integrantes", command=self.nombre_integrantes)

        self.nombre_label = tk.Label(self, text="Nombre")
        self.nombre_entry = tk.Entry(self)
        self.apellido_label = tk.Label(self, text="Apellido")
        self.apellido_entry = tk.Entry(self)
        self.dias_laborados_label = tk.Label(self, text="Dias Laborados")
        self.dias_laborados_entry = tk.Entry(self)
        self.salario_label = tk.Label(self, text="Salario")
        self.salario_entry = tk.Entry(self)
        self.aumento_label = tk.Label(self, text="Aumento")
        self.aumento_entry = tk.Entry(self)
        self.calculate_button = tk.Button(self, text="Calcular", command=self.calculate)
        self.export_button = tk.Button(self, text="Exportar a archivo", command=self.exportar_resultados)

        self.nombre_label.pack()
        self.nombre_entry.pack()
        self.apellido_label.pack()
        self.apellido_entry.pack()
        self.dias_laborados_label.pack()
        self.dias_laborados_entry.pack()
        self.salario_label.pack()
        self.salario_entry.pack()
        self.aumento_label.pack()
        self.aumento_entry.pack()
        self.calculate_button.pack()
        self.export_button.pack()

    def salir(self):
     self.destroy()

    def acerca_de_proyecto(self):
        acerca_de_proyecto_ventana = tk.Toplevel(self)
        acerca_de_proyecto_ventana.title("Acerca del proyecto")
        acerca_de_proyecto_ventana.geometry("300x200")

        texto_acerca_de_proyecto = tk.Label(acerca_de_proyecto_ventana, text="""
        Este proyecto fue desarrollado en python tkinder con POO.
        El objetivo de este proyecto es calcular las diferentes 
        prestaciones laborales de un trabajador.
        """)
        texto_acerca_de_proyecto.pack()

    def nombre_integrantes(self):
        nombre_integrantes_ventana = tk.Toplevel(self)
        nombre_integrantes_ventana.title("Nombre de los integrantes")
        nombre_integrantes_ventana.geometry("200x100")
        texto_nombre_integrantes = tk.Label(nombre_integrantes_ventana, text="""
        Yeisson Guerra
        Leandro Aristizibal
        """)
        texto_nombre_integrantes.pack()

    def calculate(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        dias_laborados = int(self.dias_laborados_entry.get())
        salario = float(self.salario_entry.get())
        aumento = float(self.aumento_entry.get())

        name_label = tk.Label(self, text=f"Nombre ->{nombre} ------- Apellido ->{apellido}")
        name_label.pack()

        trabajador = Trabajador(nombre, apellido, dias_laborados, salario, aumento)
        prima = trabajador.calcular_prima()
        result_label = tk.Label(self, text=f"Prima empleado: {prima}")
        result_label.pack()

        trabajador = Trabajador(nombre, apellido, dias_laborados, salario, aumento)
        cesantias = trabajador.calcular_cesantias()
        result_label = tk.Label(self, text=f"Censantias causadas por el empleado: {cesantias}")
        result_label.pack()

        trabajador = Trabajador(nombre, apellido, dias_laborados, salario, aumento)
        intereses = trabajador.calcular_intereses_cesantias()
        result_label = tk.Label(self, text=f"Interes de censantias causadas por el empleado: {intereses}")
        result_label.pack()

        trabajador = Trabajador(nombre, apellido, dias_laborados, salario, aumento)
        vacaciones = trabajador.calcular_vacaciones()
        result_label = tk.Label(self, text=f"Vacaciones a la fecha: {vacaciones}")
        result_label.pack()

        trabajador = Trabajador(nombre, apellido, dias_laborados, salario, aumento)
        salario_transporte = trabajador.calcular_salario_con_transporte()
        result_label = tk.Label(self, text=f"Salario con subtrasporte: {salario_transporte}")
        result_label.pack()

        trabajador = Trabajador(nombre, apellido, dias_laborados, salario, aumento)
        total_liquidacion = trabajador.calcular_total_liquidacion()
        result_label = tk.Label(self, text=f"Total Liquidacion: {total_liquidacion}")
        result_label.pack()

        self.resultados_a_exportar = f"Nombre: {nombre} {apellido}\n"
        self.resultados_a_exportar += f"Prima empleado: {prima}\n"
        self.resultados_a_exportar += f"Censantias causadas por el empleado: {cesantias}\n"
        self.resultados_a_exportar += f"Interes de censantias causadas por el empleado: {intereses}\n"
        self.resultados_a_exportar += f"Vacaciones a la fecha: {vacaciones}\n"
        self.resultados_a_exportar += f"Salario con subtrasporte: {salario_transporte}\n"
        self.resultados_a_exportar += f"Total Liquidacion: {total_liquidacion}\n"

    def exportar_resultados(self):
        exportar_resultados(self.resultados_a_exportar)


if __name__ == "__main__":
    app = Application()
    app.mainloop()