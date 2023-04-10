class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre
    def destruir(self):
        em = self.nombre
        print("Se destruye al empleado", em)
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
        ed = self.nombre
        print("Se destruye el edificio", ed)
        for empleado in self.empleados:
            empleado.destruir()
        del self
        return na
    def __str__(self):
        return self.nombre
    
class Empresa():
    def __init__(self, nombre, edificios=[]):
        self.nombre = nombre
        self.edificios = edificios
    def destruir(self):
        em = self.nombre
        print("Se destruye la empresa", em)
        for edificio in self.edificios:
            edificio.destruir()
        del self
        return em
    def __str__(self):
        return self.nombre
    

    
   


        