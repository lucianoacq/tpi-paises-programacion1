import csv

def normalizar_nombre(nombre):
    return nombre.strip().lower()

def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    fila["poblacion"] = int(fila["poblacion"])
                    fila["superficie"] = int(fila["superficie"])
                    paises.append(fila)
                except ValueError:
                    print(f"Fila inválida, se omite: {fila}")
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
    return paises


def agregar_pais(paises):
    nombre = input("Nombre del país: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    
    continente = input("Continente: ").strip()
    if continente == "":
        print("Error: el continente no puede estar vacío.")
        return
    
    try:
        poblacion = int(input("Cantidad de habitantes: "))
    except ValueError:
        print("Error: debe ingresar un número entero")
        return

    try:
        superficie = int(input(f"Ingrese la superficie de {nombre}: "))
    except ValueError:
        print("Error: debe ingresar un número entero")
        return    

    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(pais)
    print(f"'{nombre}' agregado correctamente.")


def actualizar_paises(paises):
    nombre_buscado = input("Ingrese el nombre del pais al que le quiere aplicar una actualizacion: ")
    if normalizar_nombre(nombre_buscado) == "":
        print("Error: el nombre no puede estar vacío.")
        return
        
    for pais in paises:
        if normalizar_nombre(pais["nombre"]) == normalizar_nombre(nombre_buscado):
            try:
                nueva_poblacion = int(input(f"Nueva población de {pais['nombre']}: "))
                pais["poblacion"] = nueva_poblacion
            except ValueError:
                print("Error: debe ingresar un número entero.")
                return

            try:
                nueva_superficie = int(input(f"Nueva superficie de {pais['nombre']}: "))
                pais["superficie"] = nueva_superficie
            except ValueError:
                print("Error: debe ingresar un número entero.")
                return

            print(f"'{pais['nombre']}' actualizado correctamente.")
            return

    print(f"No se encontró ningún país con el nombre '{nombre_buscado}'.")
 

def guardar_paises(paises, nombre_archivo):
    try:
        with open(nombre_archivo , "w", encoding="utf-8", newline="") as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
            print("Datos guardados correctamente.")

    except Exception as e:
        print(f"Error al guardar: {e}")
    

def menu(paises):
    while True:
        print("\n--- GESTIÓN DE PAÍSES ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Estadísticas")
        print("7. Guardar y salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_paises(paises)
        elif opcion == "7":
            guardar_paises(paises, "paises.csv")
            break
        else:
            print("Opción inválida.")



paises = cargar_paises("paises.csv")
menu(paises)