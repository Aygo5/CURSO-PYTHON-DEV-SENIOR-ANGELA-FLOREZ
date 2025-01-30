class VEHICULO:
    def __init__(self, tipo):
        self.tipo= tipo
    
    def Descripcion(self):
        return f"Este es un vehículo de tipo {self.tipo}"

class Moto(VEHICULO):
    def __init__(self, tipo, marca):
      super().__init__(tipo) #Atributo de la clase madre
      self.marca = marca

moto1= Moto("Motocicleta","Ducatti")
print(moto1.Descripcion())

    