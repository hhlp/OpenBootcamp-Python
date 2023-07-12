class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print(f"Nombre, {self.nombre}")
        print("Nota: ", self.nota)

    def valorar(self):
        if self.nota < 5:
            print(f"{self.nombre} ha suspendido")
        else:
            print(f"{self.nombre} ha aprobado")

if __name__ == "__main__":

    alumno1 = Alumno("Alumno 1", 4)
    alumno1.mostrar()
    alumno1.valorar()
    alumno2 = Alumno("Alumno 2", 7)
    alumno2.mostrar()
    alumno2.valorar()
