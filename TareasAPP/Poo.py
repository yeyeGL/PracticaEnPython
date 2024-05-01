class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completado = False

    def completar(self):
        self.completado = True

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {'Completado' if self.completado else 'No completado'}"
