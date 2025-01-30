#Método instancia -> Estoy extrayendo el objeto
#Método clase -> Me traigo toda la clase
class Animal:
    #Método constructor: Setear los valores de acuerdo a las instancias a crear
    def __init__(self, nombre, edad):
        #Instancias
        self.nombre=nombre
        self.edad=edad
    #Método
    def saludar(self):
        return f"Hola, mi animalito {self.nombre} tiene {self.edad} años de edad"
     
#Objeto    
animal1= Animal("Sasha",5)
#Imprimir un solo atributo
print(animal1.nombre)
print(animal1.edad)
#Imprimir un comportamiento
print(animal1.saludar())