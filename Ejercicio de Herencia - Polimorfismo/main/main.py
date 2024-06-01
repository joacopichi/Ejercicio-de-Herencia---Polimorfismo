from controller.empleado_controller import EmpleadoController
from controller.departamento_controller import DepartamentoController
from service.empleados import Gerente, Desarrollador, Diseñador
from service.departamentos import Desarrollo, Diseño

gerente = Gerente("John Doe", 10000)
desarrollador1 = Desarrollador("Alice Smith", 8000)
desarrollador2 = Desarrollador("Bob Johnson", 7500)
diseñador = Diseñador("Eva Brown", 7000)

desarrollo = Desarrollo("Desarrollo", [desarrollador1, desarrollador2])
diseño = Diseño("Diseño", [diseñador])

empleados = [gerente, desarrollador1, desarrollador2, diseñador]
departamentos = [desarrollo, diseño]

print("=== Empleados ===")
for empleado in empleados:
    empleado_controller = EmpleadoController(empleado)
    empleado_controller.mostrar_descripcion()

print("\n=== Departamentos ===")
for departamento in departamentos:
    departamento_controller = DepartamentoController(departamento)
    departamento_controller.mostrar_lista_empleados()
