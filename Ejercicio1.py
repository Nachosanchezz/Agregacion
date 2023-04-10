class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre
    def destruir(self):
        name = self.nombre
        print("Se destruye al empleado", name)
        del self
        return name
    def __str__(self):
        return self.nombre
    
class Edificio():
    def __init__(self, nombre, ciudad, empleados=[]):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empleados = empleados
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    def __str__(self):
        return self.nombre


        