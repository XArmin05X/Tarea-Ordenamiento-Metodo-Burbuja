# Algoritmo de Ordenamiento: Burbuja (Bubble Sort)

Este repositorio contiene una implementación en Python del método de ordenamiento de burbuja, diseñada para procesar y ordenar una lista de 50,000 números enteros extraídos de un archivo de texto.



## 1. Análisis de Complejidad

El algoritmo de burbuja es conocido por su simplicidad, pero no es el más eficiente para grandes conjuntos de datos. Su complejidad se define mediante la Notación Big O:

*   **Peor Caso $O(n^2)$:** Ocurre cuando la lista está en orden inverso. Se deben realizar $n$ pasadas y $n$ comparaciones en cada una.
*   **Caso Promedio $O(n^2)$:** En listas con orden aleatorio, la cantidad de comparaciones e intercambios sigue una progresión cuadrática.
*   **Mejor Caso $O(n)$:** Solo se logra si el algoritmo está optimizado con una bandera de control y la lista ya está ordenada. En la implementación estándar es $O(n^2)$.

Para este proyecto con **50,000 números**, el algoritmo realiza aproximadamente **1,250,000,000** de comparaciones potenciales.

## 2. Casos de Uso

¿Cuándo es recomendable usar el método de burbuja?
1.  **Fines Educativos:** Es el mejor algoritmo para introducir conceptos de algoritmos de ordenamiento y complejidad computacional.
2.  **Listas muy pequeñas:** En listas de 10 o 20 elementos, la diferencia de tiempo con algoritmos avanzados es imperceptible y el código es más sencillo de mantener.
3.  **Sistemas con recursos limitados:** Donde la simplicidad del código es crítica y no se espera procesar grandes volúmenes de información.

## 3. Comparativa Teórica: Burbuja vs. Quicksort

| Característica | Bubble Sort | Quicksort |
| :--- | :--- | :--- |
| **Complejidad Promedio** | $O(n^2)$ | $O(n \log n)$ |
| **Método** | Intercambio directo | Divide y vencerás |
| **Eficiencia** | Muy baja para grandes datos | Muy alta |
| **Uso de Memoria** | Excelente ($O(1)$ adicional) | Bueno ($O(\log n)$ por recursión) |

**Conclusión:** Mientras que el método de burbuja tarda varios segundos (o minutos) en ordenar 50,000 números, un algoritmo como Quicksort realizaría la misma tarea en milisegundos debido a su crecimiento logarítmico.
