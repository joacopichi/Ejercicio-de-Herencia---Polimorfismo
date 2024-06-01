from service.departamentos import Departamento

class DepartamentoController:
    def __init__(self, departamento):
        self.departamento = departamento

    def mostrar_lista_empleados(self):
        print(self.departamento.lista_empleados())
