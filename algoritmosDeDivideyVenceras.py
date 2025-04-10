#Busqueda binaria recortando el array, sirve para saber si en un array se encuentra un valor o no
def busquedaBinariaRecortando (array, objetivo):
    if(len(array) == 1 and array[0] != objetivo):
        return False

    mitad = len(array) // 2

    if array[mitad] == objetivo:
        return True

    elif array[mitad] > objetivo:
        return busquedaBinariaRecortando(array[:mitad], objetivo)

    elif array[mitad] < objetivo:
        return busquedaBinariaRecortando(array[mitad:], objetivo)


#Busqueda binaria con indices, nos permite saber en que posicion se encuentra un elemento dentro de el array
def busquedaBinariaIndices(array, objetivo, inicio, fin):

    if inicio > fin:
        # o return inicio si buscamos el más proximo sin pasarse
        return - 1

    mitad = (inicio + fin) // 2

    if array[mitad] == objetivo:
        return mitad

    elif array[mitad] > objetivo:
        return busquedaBinariaIndices(array, objetivo, inicio, mitad - 1)

    elif array[mitad] < objetivo:
        return busquedaBinariaIndices(array, objetivo, mitad + 1, fin)



#Algoritmos de union y mergesort para ordenar arrays en n log n
def union(array_izquierdo, array_derecho):
    i = 0
    j = 0
    array_final = []
    while i < len(array_izquierdo) and j < len(array_derecho):
        if (array_izquierdo[i] <= array_derecho[j]):
            array_final.append(array_izquierdo[i])
            i += 1
        else:
            array_final.append(array_derecho[j])
            j += 1

    # Una vez que termina de recorrer uno de los arrays simplemente añadimos el resto del array restante
    if i < len(array_izquierdo):
        return array_final + array_izquierdo[i:]
    else:
        return array_final + array_derecho[j:]


def mergeSort(array):
    if (len(array) < 2):
        return array

    else:
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]

        izquierda = mergeSort(izquierda)
        derecha = mergeSort(derecha)

        # Comprobacion previa que ahorra realizar la union en caso de que izquierda y derecha se puedan unir directamente
        if (izquierda[-1] < derecha[0]):
            return izquierda + derecha
        else:
            return union(izquierda, derecha)


