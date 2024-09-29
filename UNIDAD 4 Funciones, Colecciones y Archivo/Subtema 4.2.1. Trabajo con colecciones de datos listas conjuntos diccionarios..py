#Crear un Diccionario:
#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
#Acceder y Modificar Valores:

#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
#Verificar Existencia de Claves:

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
#Eliminar una Clave:

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
#Imprimir el Diccionario Final:

#Imprime el diccionario resultante después de realizar todas las operaciones.

print("Tarea Elaborada por: Jhon Landazuri")

# Crear el diccionario con información personal ficticia
informacion_personal= {
    "nombre": "Marco Carvajal",
    "edad": "27",
    "ciudad": "Cuenca",
    "profesion": "Arquitecto",
    "estado civil": "Soltero"
}

#Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal ["ciudad"]= "Quito"

#Agregar una nueva clave-valor al diccionario para la "profesion"
informacion_personal ["profesion"]= ("Ingeniería Civil")

# Verificar si la clave "telefono" existe en el diccionario, si no, se agraga
if "numero telefonico" not in informacion_personal:
    informacion_personal["numero telefonico"]="0943141334" #Numero telefonico ficticio
else:
    print("La clave 'numero telefonico' ya existe.")

#Eliminar clave "Edad"
del informacion_personal["edad"]

#Imprimir el diccionario Final
print("Nombre:", informacion_personal["nombre"])
print("Ciudad:", informacion_personal["ciudad"])
print("Profesión:", informacion_personal["profesion"])
print("Estado Civil:", informacion_personal["estado civil"])
print("Número Telefónico:", informacion_personal["numero telefonico"])