class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre
    def destruir(self):
        an = self.nombre
        print("Se destruye al empleado", an)
        del self
        return an
    def __str__(self):
        return self.nombre
    
class Edificio():
    def __init__(self, nombre, ciudad, empleados=[]):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empleados = empleados
    def destruir(self):
        na = self.nombre
        print("Se destruye el edificio", na)
        del self
        return na 
    for empleado in self.empleados:
        empleado.destruir()
    def __str__(self):

    
   


        