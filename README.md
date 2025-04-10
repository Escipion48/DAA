# 📚 Algoritmos - Diseño y Análisis de Algoritmos (URJC)

Este repositorio contiene una colección de implementaciones de algoritmos desarrollados durante la asignatura de **Diseño y Análisis de Algoritmos** en la **Universidad Rey Juan Carlos (URJC)**.

El objetivo del repositorio es servir como apoyo académico, facilitar el estudio de los distintos paradigmas de diseño algorítmico y mantener organizadas las prácticas y ejemplos vistos en clase.

## 🔍 Contenido

Los algoritmos se agrupan según el paradigma de diseño que siguen:

### 🔸 Algoritmos Voraces
Implementaciones que siguen una estrategia de decisión local óptima en cada paso con la esperanza de encontrar una solución global óptima.

Ejemplos típicos:
- Problema del cambio de monedas
- Actividades compatibles
- Huffman

### 🔸 Algoritmos Voraces en Grafos
Aplicaciones de la estrategia voraz en estructuras de grafos.

Ejemplos típicos:
- Kruskal
- Prim
- Dijkstra

### 🔸 Divide y Vencerás
Algoritmos que dividen el problema en subproblemas más pequeños, los resuelven recursivamente y combinan los resultados.

Ejemplos típicos:
- Merge Sort
- Quick Sort
- Binary Search

### 🔸 Backtracking
Algoritmos que exploran todas las posibles soluciones mediante búsqueda exhaustiva, descartando aquellas que no cumplen las condiciones.

Ejemplos típicos:
- N-Reinas
- Sudoku Solver
- Problema de la Mochila (versión backtracking)

## 🛠️ Tecnologías
- Lenguaje principal: Python (aunque se pueden incluir versiones en C++ o Java si se requiere)
- Organización modular por carpetas
- Comentarios explicativos en cada implementación

## 📁 Estructura del repositorio

```plaintext
algoritmos-urjc/
│
├── voraces/
│   ├── cambio_monedas.py
│   └── actividades.py
│
├── voraces_grafos/
│   ├── kruskal.py
│   ├── prim.py
│   └── dijkstra.py
│
├── divide_y_venceras/
│   ├── mergesort.py
│   └── quicksort.py
│
├── backtracking/
│   ├── n_reinas.py
│   └── sudoku.py
│
└── README.md
