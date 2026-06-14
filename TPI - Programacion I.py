# Parte A


import csv


# Convierte un nombre a minúsculas y sin espacios al principio/final,
# para poder comparar nombres sin importar mayúsculas o espacios extra.
def normalizar_nombre(nombre):
    return nombre.strip().lower()

# Lee el archivo CSV indicado y devuelve una lista de diccionarios (uno por país).
# Convierte población y superficie a enteros.
# Si el archivo no existe, o una fila tiene datos inválidos, lo informa y continúa
# sin interrumpir la carga del resto de los países.
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    # Convertimos población y superficie de string a entero
                    fila["poblacion"] = int(fila["poblacion"])
                    fila["superficie"] = int(fila["superficie"])
                    paises.append(fila)
                except ValueError:
                    print(f"Fila inválida, se omite: {fila}")
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
    return paises


# Pide al usuario los datos de un país nuevo (nombre, continente, población,
# superficie), valida que no haya campos vacíos ni datos inválidos,
# y lo agrega a la lista de países.
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

    # Armamos el diccionario del país y lo agregamos a la lista
    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(pais)
    print(f"'{nombre}' agregado correctamente.")


# Busca un país por nombre (coincidencia exacta, sin importar mayúsculas/espacios)
# y permite actualizar su población y superficie.
# Si no se encuentra el país, informa al usuario.
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
 

# Escribe la lista de países en el archivo CSV indicado, sobrescribiendo
# su contenido anterior. Maneja errores que puedan ocurrir al escribir.
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
    

# Muestra el menú principal y procesa la opción elegida por el usuario,
# llamando a la función correspondiente. Se repite hasta que el usuario
# elige guardar y salir (opción 7).
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
        elif opcion == "3":
            buscar_por_nombre(paises)
        elif opcion == "4":
            menu_filtros(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            guardar_paises(paises, "paises.csv")
            break
        else:
            print("Opción inválida.")


# Parte B

def buscar_por_nombre(paises):
    busc_pais_nom = input("Ingrese el nombre del país que desea buscar: ").strip().lower()
    if busc_pais_nom == "":
        print("¡El nombre del país no puede estar vacío!")
        return
    
    resultados = []
    for pais in paises:
        if busc_pais_nom in pais["nombre"].lower():
            resultados.append(pais)

    if not resultados:
        print("¡No se encontraron países con ese nombre!")

    else:
        for pais in resultados:
            print(pais)

def filtrar_por_continente(paises):
    busc_cont_nom = input("Ingrese el nombre del continente que desea buscar: ").strip().lower()
    if busc_cont_nom == "":
        print("¡El nombre del continente no puede estar vacío!")
        return
    
    resultados = []
    for pais in paises:
        if pais["continente"].lower() == busc_cont_nom.lower():
            resultados.append(pais)

    if not resultados:
        print("¡No se encontraron continentes con ese nombre!")

    else:
        for pais in resultados:
            print(pais)

def filtrar_por_poblacion(paises):
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))

    except ValueError:
        print("ERROR: Debe ingresar números enteros.")
        return
    
    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo: 
            resultados.append(pais)

    if not resultados:
        print("¡No se encontraron países en ese rango de población!")

    else:
        for pais in resultados:
            print(pais)

def filtrar_por_superficie(paises):
    try:
        minimo = int(input("Superficie mínima (km²): "))
        maximo = int(input("Superficie máxima (km²): "))

    except ValueError:
        print("Error: ingrese números enteros.")

        return
    
    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if not resultados:
        print("¡No se encontraron países en ese rango de superficie!")

    else:
        for pais in resultados:
            print(pais)

def menu_filtros(paises):
    print("\n--- FILTRAR POR ---")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
    else:
        print("Opción inválida.")

def ordenar_paises(paises):
    print("\n--- ORDENAR POR ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    criterio = input("Criterio: ").strip()
    
    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if criterio not in campos:
        print("Opción inválida.")
        return
    
    direccion = input("¿Orden ascendente? (S/N): ").strip().lower()

    if direccion == "n":
        reverse = True

    else:
        reverse = False

    ordenados = sorted(paises, key=lambda p: p[campos[criterio]], reverse=reverse)

    for pais in ordenados:
        print(pais)

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países cargados.")
        return

    
    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_poblacion = 0
    total_superficie = 0
    continentes = {}

    for pais in paises:
        
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais

        total_poblacion = total_poblacion + pais["poblacion"]
        total_superficie = total_superficie + pais["superficie"]

        con = pais["continente"]

        if con in continentes:
            continentes[con] = continentes[con] + 1

        else:
            continentes[con] = 1

    promedio_pob = total_poblacion / len(paises)
    promedio_sup = total_superficie / len(paises)

    print("País con mayor población: " + mayor_pob["nombre"])
    print("País con menor población: " + menor_pob["nombre"])
    print("Promedio de población: " + str(int(promedio_pob)))
    print("Promedio de superficie: " + str(int(promedio_sup)) + " km²")
    print("Cantidad de países por continente:")

    for continente in continentes:
        print("  " + continente + ": " + str(continentes[continente]))


paises = cargar_paises("paises.csv")
menu(paises)
