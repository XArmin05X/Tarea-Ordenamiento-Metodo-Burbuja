import time

def bubble_sort(lista):
    n = len(lista)
    # El algoritmo de burbuja recorre la lista varias veces
    for i in range(n):
        # En cada pasada, el elemento más grande "flota" hasta su posición correcta
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Leemos cada línea, eliminamos espacios y convertimos a entero
            numeros = [int(linea.strip()) for linea in archivo if linea.strip()]
        return numeros
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return []
    except ValueError:
        print("Error: El archivo contiene datos que no son números válidos.")
        return []

def main():
    nombre_archivo = "datos.txt"
    
    # 1. Cargar los datos
    print("Cargando datos...")
    datos = leer_archivo(nombre_archivo)
    
    if not datos:
        return

    print(f"Se han cargado {len(datos)} números.")
    print("Iniciando ordenamiento... (Tiempo de espera largo debido a la dificultad de procesamiento del método de burbuja)")

    # 2. Medir el tiempo de inicio
    # Usamos perf_counter para mayor precisión
    inicio = time.perf_counter()

    # 3. Ejecutar el ordenamiento
    bubble_sort(datos)

    # 4. Medir el tiempo de fin
    fin = time.perf_counter()

    # 5. Calcular la diferencia en milisegundos
    tiempo_ms = (fin - inicio) * 1000

    print(f"\nOrdenamiento completado.")
    print(f"Tiempo transcurrido: {tiempo_ms:.2f} milisegundos.")
    
    # Opcional: Guardar los resultados ordenados o imprimir los primeros 10
    # print("Primeros 10 números ordenados:", datos[:10])

if __name__ == "__main__":
    main()
