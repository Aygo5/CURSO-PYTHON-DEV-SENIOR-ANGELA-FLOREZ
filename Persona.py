#Método de clases
class Persona:
    cantidadEmpleados=0

    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        Persona.cantidadEmpleados+=1

    @classmethod
    def totalEmpleados(cls):
        return f"Tengo {cls.cantidadEmpleados} empleados."

empleado1= Persona("Laura",21)
empleado2= Persona("Santiago",20)

print(empleado1.nombre)
print(Persona.totalEmpleados())
