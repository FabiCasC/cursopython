class Empleado: 
    def __init__(self, nombre, salario): 
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado): 
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def mostrar_informacion(self): 
        return f"{self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}"
    
gerente_1 = Gerente("Carlos", 1500, "Analítica")
print(gerente_1.mostrar_informacion())