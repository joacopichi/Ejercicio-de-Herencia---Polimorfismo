from service.empleados import Empleado

class EmpleadoController:
    def __init__(self, empleado):
        self.empleado = empleado

    def mostrar_descripcion(self):
        print(self.empleado.descripcion())
