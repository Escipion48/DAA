# Algoritmo: Conteo de Componentes Conexas (Connected Components Counting)
# Método: DFS modificado con eliminación de nodos no visitados

def recorrer_nodos_conexos(grafo, inicio, nodos): #DFS modificado para que solo recorra todos los nodos conexos a un nodo
    cola_de_prioridad = [inicio]
    while cola_de_prioridad:
        nodo_actual = cola_de_prioridad.pop()
        nodos.remove(nodo_actual) #En vez de una lista de visitados una lista de no visitados, nos ayuda a reducir la carga despues en el contador
        for nombre in grafo[nodo_actual]:
            if nombre in nodos and nombre not in cola_de_prioridad:
                cola_de_prioridad.append(nombre)
    return nodos #Devolvemos nodos que no se han asignado al grupo


def contador_grupos_nodos(grafo): #Utilizando nuestro DFS modificado recorremos todos los nodos del grafo para saber cuantos grupos hay
    conteo = 0
    nodos = list(grafo.keys())
    while nodos:
        nodos = recorrer_nodos_conexos(grafo, nodos[0], nodos)
        conteo += 1
    return conteo