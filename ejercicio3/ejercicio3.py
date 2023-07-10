#escriba un script que sea capaz de calcular el índice de masa corporal de una persona en base a los datos ingresados por el usuario.
 
import math
from tabulate import tabulate
 
peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))
 
IMC = round(peso/math.pow(estatura,2),1)
 
print("Su IMC es de "+str(IMC))
 
lista = [["Composición corporal","Índice de masa corporal (IMC)"],["Peso inferior al normal","Menos de 18.5"],["Normal","18.5 – 24.9"],["Peso superior al normal","25.0 – 29.9"],["Obesidad","Más de 30.0"]]
 
print(tabulate(lista))
