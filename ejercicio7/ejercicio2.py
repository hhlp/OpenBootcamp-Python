import time 
import datetime

actual = time.strftime('%H:%M:%S')
salida = time.strftime('19:00:00')

ha = datetime.datetime.strptime(actual, '%H:%M:%S')
hs = datetime.datetime.strptime(salida, '%H:%M:%S')

if ha >= hs:
    print("Es Hora de Salir")
else:
    faltante = hs - ha
    print("Faltan :", faltante, "para la salida")
