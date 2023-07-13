file = open('archivo.txt', 'w')
file.write('escribir archivo!\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('segunda vez\n')

file.seek(0)
print(file.read())
file.close()
