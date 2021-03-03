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


def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()

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



def askSampleList(catalog):
    """Le pregunta al usuario respecto al tamaño de la muestra sobre la que se desea aplicar una función."""

    n_sample = input("Ingrese el tamaño de la muestra sobre la que desea indagar (recuerde que este no debe exceder la cantidad de videos en el catálogo): ")

    if int(n_sample) > lt.size(catalog['videos']):
        
        print("El número de muestra ha superado el tamaño de la lista, se procederá con la cantidad máxima de videos dentro del catálogo: {}".format(lt.size(catalog['videos'])))

        n_sample = lt.size(catalog['videos'])-1
        
    return int(n_sample)



def sortVideos(catalog, size):
    """
    Organiza los videos mediante Merge Sort
    """
    return controller.sortVideos(catalog, size)


def filterCategory(catalog):
    """Le pregunta al usuario bajo que categoría desea filtrar los algoritmos."""


    filter_category = input("Ingrese el nombre de la categoria con la que desea filtrar sus datos: ").lower()

    for category in lt.iterator(catalog['categories']):

        if filter_category == category["name"].strip().lower():

            return category["name"].strip()

    print("Este no es el nombre de una categoría existente. Intente de nuevo.")
    filterCategory(catalog)


def filterCountry(catalog):
    """Le pregunta al usuario bajo que país desea filtrar los algoritmos."""

    filter_country = input("Ingrese el nombre del país con el que desea filtrar sus datos: ")

    return filter_country

def printResultsReq1(video_list, n_sample):

    a="1. trending_date"
    b="2. title"
    c = "3. channel_title"
    d = "4. publish_time"
    e = "5. views"
    f = "6. likes"
    g = "7. dislikes"
    
    formato="|{}|{}|{}|{}|{}|{}|{}|\n".format(a.center(10),b.center(10),c.center(10),d.center(10),e.center(10),f.center(10),g.center(10))+("-"*130)+"\n"

    texto="\n"+formato
    
    size = lt.size(video_list)

    if size > n_sample:
        print("Los primeros ", n_sample, " videos ordenados por número de visitas son:")
        i=1
        while i <= n_sample:
            video = lt.getElement(video_list, i)

            formato="|{}|{}|{}|{}|{}|{}|{}|\n".format(video["trending_date"].center(6),video["title"].center(6), video["channel_title"].center(6), video["publish_time"].center(6), video["views"].center(6), video["likes"].center(6), video["dislikes"].center(6))+("-"*130)+"\n"

            texto+=formato

            i+=1

    print(texto)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("Cargando información de los archivos ....\n") 
        catalog = initCatalog()
        loadData(catalog)

        print('Videos cargados: ' + str(lt.size(catalog['videos'])) + "\n")
        
        print("Información del primer video cargado:  ")
        print("| Título: {} | Nombre del canal: {} | Fecha en tendencia: {} | País: {} | Visitas: {} | Likes: {} | Dislikes: {}\n".format(*FirstVideoData(catalog)))

        print('Categorías cargadas: ' + str(lt.size(catalog["categories"])))
        show_categories(catalog)



    elif int(inputs[0]) == 2:

        filter_category = filterCategory(catalog)
        filter_country = filterCountry(catalog)

        filtered_catalog = controller.filterCatalog(catalog = catalog, column_1 = "category_name", column_2 = "country", value_1 = filter_category, value_2 = filter_country)

        n_sample = askSampleList(filtered_catalog)

        top_views = sortVideos(filtered_catalog, lt.size(filtered_catalog["videos"]))
        
        printResultsReq1(top_views[1], n_sample)

    else:
        sys.exit(0)
sys.exit(0)

