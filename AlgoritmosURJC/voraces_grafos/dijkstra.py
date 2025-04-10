# Esta por estar no se si funciona :)

def dijkstra_with_track(grafo, inicio):
    NOMBRE = 0; PESO = 1
    nodos = set(grafo.keys())
    visitados = set()
    pesos = {i: (float('inf'), "anterior") for i in nodos}
    cola_de_prioridad = []
    cola_de_prioridad.append((inicio, 0))
    pesos[inicio] = (0, inicio)
    while visitados != nodos:
        nombre, peso = cola_de_prioridad.pop()
        visitados.add(nombre)
        for nodo in grafo[nombre]:
            if nodo[NOMBRE] not in visitados:
                cola_de_prioridad.append((nodo[NOMBRE], nodo[PESO] + peso))
                cola_de_prioridad.sort(key=lambda x: x[PESO], reverse=True)
            if nodo[PESO] + peso < pesos[nodo[NOMBRE]][0]:
                pesos[nodo[NOMBRE]] = (nodo[PESO] + peso, nombre)
    return pesos

def dijkstra_backtraking(pesos, inicio, final):
    track = []
    track.append(final)
    camino = pesos[final][1]
    track.append(camino)
    while camino != inicio:
        camino = pesos[camino][1]
        track.append(camino)
    track.reverse()
    return track