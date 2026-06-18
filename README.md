# Gestión de Datos de Países en Python
Trabajo Práctico Integrador - Programación I

Tecnicatura Universitaria en Programación (UTN - Modalidad a Distancia)

## Descripción

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia Programación 1. Se trata de un sistema en consola que permite gestionar información de distintos países, incluyendo su nombre, población, superficie en km² y continente al que pertenecen.
El programa lee los datos desde un archivo CSV al iniciar, y desde un menú interactivo el usuario puede agregar nuevos países, actualizar la población y superficie de los existentes, buscar países por nombre, aplicar filtros (por continente o por rangos de población y superficie), ordenar el listado según distintos criterios, y consultar estadísticas generales sobre el conjunto de datos.
El objetivo principal del trabajo fue aplicar y afianzar los conceptos vistos durante la materia: listas, diccionarios, funciones, estructuras condicionales y repetitivas, manejo de archivos, ordenamientos y cálculo de estadísticas básicas.


## Cómo ejecutar
Para correr el programa, es necesario tener instalado Python 3. Desde la terminal, parado en la carpeta del proyecto, ejecutar:
`python "TPI - Programacion I.py"`
Es importante que el archivo `paises.csv` se encuentre en la misma carpeta que el archivo principal, ya que el programa lo busca automáticamente al iniciar para cargar los datos.


## Ejemplo de uso
A continuación se muestra un ejemplo de cómo se ve la búsqueda de un país por nombre:

Seleccione una opción: 3
Ingrese el nombre del país que desea buscar: japon
{'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'}

Como se puede ver, la búsqueda no distingue entre mayúsculas y minúsculas, y devuelve el país encontrado con todos sus datos.


## Integrantes
Este trabajo fue realizado por:

- Luciano Acquaviva (Parte A): carga de datos desde CSV, alta de países, actualización de población y superficie, guardado de datos y menú principal.
- Alejo Giannini (Parte B): búsqueda de países, filtros por continente/población/superficie, ordenamiento y estadísticas.

## Documentación y video

- Documentación en PDF: [Informe Teorico - TPI Programacion I.pdf](./Informe%20Teorico%20-%20TPI%20Programacion%20I.pdf)
- Video demostrativo: https://www.youtube.com/watch?v=k1suDdM4U8I