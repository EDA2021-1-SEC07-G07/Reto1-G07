"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información de los videos en el catálogo")
    print("2- Videos en tendencia con más views (País y Categoría)")
    print("3- Video con record de tendencia (País)")
    print("4- Video con record de tendencia (Categoría)")
    print("5- Videos con más likes (País y Categoría)")
    print("0- Salir de la aplicación.")


def initCatalog(list_type):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(list_type)

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def show_categories(catalog):
    
    a="Id"
    b="Nombre de Categoría"
    
    formato="|{}|{}|\n".format(a.center(6),b.center(26))+("-"*36)+"\n"

    texto=("-"*36)+"\n"+formato
    
    actual_node= lt.firstElement(catalog["categories"])

    for i in range(1,lt.size(catalog["categories"])):
        actual_node_id=actual_node["category_id"]
        actual_node_name=actual_node["name"]

        formato="|{}|{}|\n".format(actual_node_id.center(6),actual_node_name.center(26))+("-"*36)+"\n"

        texto+=formato

        actual_node= lt.getElement(catalog["categories"], i+1)
 
    print(texto)



def FirstVideoData(catalog):

   
    first_video = lt.firstElement(catalog["videos"])
    title =  first_video["title"]
    channel_title =  first_video["channel_title"]
    trending_date =  first_video["trending_date"]
    country =  first_video["country"]
    views =  first_video["views"]
    likes =  first_video["likes"]
    dislikes =  first_video["dislikes"]

    return (title, channel_title, trending_date, country, views, likes, dislikes)

def askListType():
    """Le pregunta al usuario respecto al tipo de lista que este desee usar."""

    list_type = None

    print("Elija con que tipo de lista desea que se cargue el catálogo de videos:\n")
    print("1- Array List")
    print("2- Single Linked List")

    seleccion_lista = input('Seleccione una opción para continuar\n')

    if int(seleccion_lista[0]) == 1:
        
        list_type = "ARRAY_LIST"

    elif int(seleccion_lista[0]) == 2:

        list_type = "LINKED_LIST"

    else:
        sys.exit(0)

    return list_type


def askSampleList(catalog):
    """Le pregunta al usuario respecto al tamaño de la muestra sobre la que se desea aplicar una función."""

    n_sample = input("Ingrese el tamaño de la muestra sobre la que desea indagar (recuerde que este no debe exceder la cantidad de videos en el catálogo): ")

    if int(n_sample) > lt.size(catalog['videos']):
        
        print("El número de muestra ha superado el tamaño de la lista, se procederá con la cantidad máxima de videos dentro del catálogo: {}".format(lt.size(catalog['videos'])))

        n_sample = lt.size(catalog['videos'])
        
    return int(n_sample)


def askSortingAlgorithm():
    """Le pregunta al usuario respecto a que tipo de algoritmo de ordenamiento desea usar."""

    sorting_algorithm = None


    print("¿Con que tipo de algoritmo desea realizar su búsqueda?")
    print("1- Algoritmo Iterativo")
    print("2- Algoritmo Recursivo")
    tipo_algoritmo = input('Seleccione una opción para continuar\n')

    if int(tipo_algoritmo[0]) == 1:

        print("Elija con que algoritmo de ordenamiento iterativo desea realizar su busqueda:\n")
        print("1- Selection Sort")
        print("2- Insertion Sort")
        print("3- Shell Sort")

        seleccion_algoritmo = input('Seleccione una opción para continuar\n')
        if int( seleccion_algoritmo[0]) == 1:

            sorting_algorithm = "SELECTION"

        elif int(seleccion_algoritmo[0]) == 2:

            sorting_algorithm = "INSERTION"

        elif int(seleccion_algoritmo[0]) == 3:

            sorting_algorithm = "SHELL"

        else:
            sys.exit(0)


    elif int(tipo_algoritmo[0]) == 2:
        print("Elija con que algoritmo de ordenamiento recursivo desea realizar su busqueda:\n")
        print("1- Merge Sort")
        print("2- Quick Sort")
        seleccion_algoritmo = input('Seleccione una opción para continuar\n')

        if int( seleccion_algoritmo[0]) == 1:
            sorting_algorithm = "MERGE"

        elif int(seleccion_algoritmo[0]) == 2:
            sorting_algorithm = "QUICK"

        else:
            sys.exit(0)

    return sorting_algorithm


def sortVideos(catalog, size, sorting_algorithm):
    """
    Organiza los videos bajo un algoritmo determinado
    """
    return controller.sortVideos(catalog, size, sorting_algorithm)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        list_type = askListType()

        print("Cargando información de los archivos ....\n") 
        catalog = initCatalog(list_type)
        loadData(catalog)

        print('Videos cargados: ' + str(lt.size(catalog['videos'])) + "\n")
        
        print("Información del primer video cargado:  ")
        print("| Título: {} | Nombre del canal: {} | Fecha en tendencia: {} | País: {} | Visitas: {} | Likes: {} | Dislikes: {}\n".format(*FirstVideoData(catalog)))

        print('Categorías cargadas: ' + str(lt.size(catalog["categories"])))
        show_categories(catalog)



    elif int(inputs[0]) == 2:

        n_sample = askSampleList(catalog)

        sorting_algorithm = askSortingAlgorithm()
    
        print("Buscando el top {} de videos tendencia con más views organizados mediante {} SORTING...".format(n_sample, sorting_algorithm))

        top_views = sortVideos(catalog, n_sample, sorting_algorithm)
        
        execution_time = top_views[0]
       
        print("El tiempo total de ejecución con el algoritmo {} SORT y el tipo de lista {} fue de: {} ms".format(sorting_algorithm, list_type,execution_time))

    else:
        sys.exit(0)
sys.exit(0)

