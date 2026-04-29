import time

# Implementación del algoritmo de ordenamiento de burbuja
def bubble_sort(lista):
    n = len(lista)
    # Recorremos toda la lista
    for i in range(n):
        # El último elemento ya está en su lugar, así que restamos i
        for j in range(0, n - i - 1):
            # Intercambiamos si el elemento actual es mayor al siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Función para cargar los 50,000 números desde el archivo txt
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # List comprehension para limpiar espacios y convertir a entero
            return [int(linea.strip()) for linea in archivo if linea.strip()]
    except Exception as e:
        print(f"Error en la lectura: {e}")
        return []

def main():
    nombre_archivo = "datos.txt"
    datos = leer_archivo(nombre_archivo)
    
    if datos:
        print(f"Iniciando ordenamiento de {len(datos)} elementos...")
        
        # Inicio de la toma de tiempo
        inicio = time.perf_counter()
        
        bubble_sort(datos)
        
        # Fin de la toma de tiempo
        fin = time.perf_counter()
        
        # Cálculo de milisegundos
        tiempo_ms = (fin - inicio) * 1000
        
        print("Ordenamiento finalizado con éxito.")
        print(f"Tiempo de ejecución: {tiempo_ms:.2f} ms")

if __name__ == "__main__":
    main()
