#En esta tarea, realizarás operaciones de lectura y escritura en archivos de texto en Python. Sigue las instrucciones detalladas a continuación:

#Escritura de Archivo de Texto:
#Crea un nuevo archivo llamado my_notes.txt.


print("Tarea Semana 16 Realizada por: Jhon Landazuri")

file_name= "my_notes.txt"

archivo_escritura = open (file_name, "w")

#Escribe al menos tres líneas de notas personales en el archivo.
archivo_escritura.write("Mi deporte favorito es: El futbol, por lo general lo práctico cada fin de semana. \n")
archivo_escritura.write("Mi hobbie es: Ver anime y jugar video juegos. \n")
archivo_escritura.write("Que haces en tus tiepos libre: Deporte, ver televisión y salir a pasear con mi hijo. \n")
archivo_escritura.write("Que genero de musíca te gusta: De mi parte no tengo un gusto exacto por la musíca, si tiene una buena letra y ritmo es sufiiciente. \n")

#Cierre del archivo
archivo_escritura.close()

#Lectura de Archivo de Texto:
archivo_lectura = open (file_name, "r")

#Método read

archivo_lectura.seek(0), #Reiniciamos el cursor desde el inicio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()
linea_4 = archivo_lectura.readline()

#Abrimos el archivo para leerlo en la consola

archivo_lectura = open (file_name, "r")

# Leemos y mostramos el contenido para para verificar

contenido =  archivo_lectura.read()
print("Contenido del Archivo despues de escribir: ")
print(contenido)

# Cerramos el archivo después de leer
archivo_lectura.close()
