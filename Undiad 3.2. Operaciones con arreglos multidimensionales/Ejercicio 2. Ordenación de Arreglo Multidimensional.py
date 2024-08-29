#Elaborado por: Jhon Landazuri
#Ordenar Arreglo Multidimensional

print("Tarea Semaa 11: Ejercicio 2")
matriz = [
    [7, 4, 99],
    [9, 69, 10],
    [11, 42, 5]
]
print(matriz)

#Se realizara el metodo de ordenamiento buble_sort

def buble_sort(fila):
    #Elaboracion del algoritmo buble Sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] > fila[i]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)
print("Matriz Original")
print(matriz)
buble_sort(matriz[2])
print(matriz)


