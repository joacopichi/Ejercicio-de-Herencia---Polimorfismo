from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @abstractmethod
    def descripcion(self):
        pass

class Gerente(Empleado):
    def descripcion(self):
        return f"Soy el gerente {self.nombre} y mi salario es ${self.salario}"

class Desarrollador(Empleado):
    def descripcion(self):
        return f"Soy el desarrollador {self.nombre} y mi salario es ${self.salario}"

class Diseñador(Empleado):
    def descripcion(self):
        return f"Soy el diseñador {self.nombre} y mi salario es ${self.salario}"
