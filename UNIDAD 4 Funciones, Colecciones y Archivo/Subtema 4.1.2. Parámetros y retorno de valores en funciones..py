#Creación de la Función:
#Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
#La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
#La función debe devolver el monto del descuento calculado.
print ("Tarea Semana 14: Jhon Landazuri")

# Definimos la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamadas a la función

monto_1 = 150  # primer monto de la compra
descuento_1 = calcular_descuento(monto_1)  # usando el valor predeterminado del 10%
monto_final_1 = monto_1 - descuento_1

monto_2 = 300  # segundo monto de la compra
porcentaje_descuento_2 = 20  # porcentaje de descuento personalizado
descuento_2 = calcular_descuento(monto_2, porcentaje_descuento_2)
monto_final_2 = monto_2 - descuento_2

# Muestra los resultados
print(f"Compra 1: El precio total de su compra es: ${monto_1}")
print(f"El descuento obtenido sera de: ${descuento_1}")
print(f"El precio final de su compra es: ${monto_final_1}")
print(f"Compra 2: El precio total de su compra es: ${monto_2}")
print(f"El descuento obtenido sera de: ${descuento_2}")
print(f"El precio final de su compra es: ${monto_final_2}")