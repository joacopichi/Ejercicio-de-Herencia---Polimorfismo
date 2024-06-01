from abc import ABC, abstractmethod

class Departamento(ABC):
    def __init__(self, nombre, empleados):
        self.nombre = nombre
        self.empleados = empleados

    @abstractmethod
    def lista_empleados(self):
        pass

class Desarrollo(Departamento):
    def lista_empleados(self):
        return f"Empleados del departamento de Desarrollo: {', '.join([empleado.nombre for empleado in self.empleados])}"

class Diseño(Departamento):
    def lista_empleados(self):
        return f"Empleados del departamento de Diseño: {', '.join([empleado.nombre for empleado in self.empleados])}"
