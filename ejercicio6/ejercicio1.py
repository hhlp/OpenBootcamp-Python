class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "El vehiculo de color {}, con {} ruedas y {} puertas".format(self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} Cv y velocidad de {}".format(self.cilindrada, self.velocidad)

mi_Vehiculo = Vehiculo("rojo", "5", "4")
print(mi_Vehiculo)

mi_Coche = Coche("rojo", "4",  "5", "300", "1400")
print(mi_Coche)
