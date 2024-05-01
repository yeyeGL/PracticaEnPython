class Trabajador:
    def __init__(self, nombre, apellido, dias_laborados, salario, aumento):
        self.nombre = nombre
        self.apellido = apellido
        self.dias_laborados = dias_laborados
        self.salario = salario
        self.aumento = aumento

    def calcular_prima(self):
        prima = (self.salario * self.dias_laborados) / 360
        return round(prima, 1)

    def calcular_cesantias(self):
        cesantias = (self.salario * self.dias_laborados) / 360
        return round (cesantias,1)

    def calcular_intereses_cesantias(self):
        cesantias = self.calcular_cesantias() 
        intereses = (cesantias * self.dias_laborados * 0.12) / 360
        return round (intereses,1)

    def calcular_vacaciones(self):
        vacaciones = (self.salario * self.dias_laborados) / 720
        return round( vacaciones,1)

    def calcular_salario_aumento(self):
        salario_aumento = self.salario * (1 + self.aumento/100)
        return round( salario_aumento,1)

    def calcular_salario_con_transporte(self):
        subsidio_transporte = 140606
        salario_aumento = self.calcular_salario_aumento()
        salario_transporte = salario_aumento + subsidio_transporte
        return round (salario_transporte,1)

    def calcular_total_liquidacion(self):
        prima = self.calcular_prima()
        cesantias = self.calcular_cesantias()
        intereses_cesantias = self.calcular_intereses_cesantias()
        vacaciones = self.calcular_vacaciones()
        total_liquidacion = prima + cesantias + intereses_cesantias + vacaciones
        return round (total_liquidacion,1)
    
"""Objeto para verificar que si este bien esta vuelta

trabajador = Trabajador("Juan", "Pérez", 360, 800000, 10)

prima = trabajador.calcular_prima()
cesantias = trabajador.calcular_cesantias()
intereses_cesantias = trabajador.calcular_intereses_cesantias()
vacaciones = trabajador.calcular_vacaciones()
salario_aumento = trabajador.calcular_salario_aumento()
salario_transporte = trabajador.calcular_salario_con_transporte()
total_liquidacion = trabajador.calcular_total_liquidacion()

print(f"Nombre: {trabajador.nombre} {trabajador.apellido}")
print(f"Prima: {prima}")
print(f"Cesantías: {cesantias}")
print(f"Intereses de cesantías: {intereses_cesantias}")
print(f"Vacaciones: {vacaciones}")
print(f"Salario con aumento: {salario_aumento}")
print(f"Salario con subsidio de transporte: {salario_transporte}")
print(f"Total liquidación: {total_liquidacion}")

"""