from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


coche = Vehiculo("Azul", "4")
print(coche)

file = open('vehiculo.bin', 'w+b')
dump(coche, file)
file.close()

file = open('vehiculo.bin', 'rb')

file.seek(0)
nuevo_coche = load(file)
file.close()

print(nuevo_coche)
