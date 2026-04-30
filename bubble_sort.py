import time

def bubble_sort(lista):
    """
    Implementación del algoritmo de ordenamiento de burbuja.
    Recorre la lista comparando elementos adyacentes y los intercambia 
    si están en el orden incorrecto.
    """
    n = len(lista)
    # Bucle externo para recorrer toda la lista
    for i in range(n):
        # Bucle interno: el rango se reduce en cada pasada porque el 
        # elemento más grande ya estará al final.
        for j in range(0, n - i - 1):
            # Comparación de elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Intercambio de posición (Swap)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def leer_archivo(nombre_archivo):
    """
    Carga datos numéricos desde un archivo de texto.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Comprensión de lista para limpiar y convertir los datos
            numeros = [int(linea.strip()) for linea in archivo if linea.strip()]
        return numeros
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
        return []
    except ValueError:
        print("Error: El archivo contiene datos no válidos.")
        return []

def main():
    nombre_archivo = "datos.txt"
    
    print("--- Algoritmo de Burbuja ---")
    print("Cargando datos...")
    datos = leer_archivo(nombre_archivo)
    
    if not datos:
        return

    print(f"Registros cargados: {len(datos)}")
    print("Ordenando... (Este proceso puede ser lento para grandes volúmenes)")

    # Medición de rendimiento
    inicio = time.perf_counter()
    bubble_sort(datos)
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000

    print(f"\nOrdenamiento completado exitosamente.")
    print(f"Tiempo total: {tiempo_ms:.2f} ms.")

if __name__ == "__main__":
    main()
