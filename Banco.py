class Banco:
    tasa_de_interes = 0.03

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def cambioTasa(cls, nueva_tasa):
        cls.tasa_de_interes = nueva_tasa

    @staticmethod
    def convertidorDinero(dolares):
        return dolares * 0.5


# Crear una instancia de Banco
cliente1 = Banco("Angela")

# Convertir dólares usando el método estático
conversion = Banco.convertidorDinero(5)
print(f"Conversión de dólares: {conversion}")  # Debería imprimir: 2.5

# Cambiar la tasa de interés usando el método de clase
Banco.cambioTasa(0.7)
print(f"Nueva tasa de interés: {Banco.tasa_de_interes}")