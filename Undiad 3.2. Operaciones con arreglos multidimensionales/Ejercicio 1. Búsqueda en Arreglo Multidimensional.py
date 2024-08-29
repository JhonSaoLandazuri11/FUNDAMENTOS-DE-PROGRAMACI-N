#Elaborado por: Jhon Landazuri
#Crear una Matriz
print("Tarea Semaa 11: Ejercicio 1")
matriz = [
    [11, 2, 23],
    [22, 1, 00],
    [27, 1, 1]
]
print(matriz)

#Función para buscar valor especifíco

def buscar_valor_seleccionado (matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j

valor_buscado = 00

if valor_buscado == valor_buscado:
    print("Valor encontrado en la posición", buscar_valor_seleccionado(matriz, valor_buscado))
else:
    print("Valor no encontrado")
