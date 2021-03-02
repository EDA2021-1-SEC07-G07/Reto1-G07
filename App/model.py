"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort 
from DISClib.Algorithms.Sorting import selectionsort 
from DISClib.Algorithms.Sorting import insertionsort 
from DISClib.Algorithms.Sorting import mergesort 
from DISClib.Algorithms.Sorting import quicksort 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(list_type):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """

    catalog={"videos":None,
            "id_videos":None,
            "categories": None,
            "videos_categories":None, }

    catalog["videos"]=lt.newList()
    catalog["id_videos"]=lt.newList(list_type,None)
    catalog["categories"]=lt.newList(list_type,None)
    catalog["videos_categories"]=lt.newList(list_type)
    return catalog



# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    
    # Se modifica el video antes de que este sea añadido al catalogo principal
    #Esto con el objetivo de añadirle una columna que indique el nombre de su categoría
    video = addVideoCategory(catalog, video)

    # Se adiciona el video modificado a la lista de videos
    lt.addLast(catalog['videos'], video)



        
def addCategory(catalog, category):
    """
    Adiciona unas category a la lista de categories
    """
    t=newCategory(category["name"], category["id"])
    lt.addLast(catalog["categories"], t)

def addVideoCategory(catalog, video):

    video_category = newVideoCategory(catalog["categories"], video)
    video["category_name"] = video_category
    return video


# Funciones para creacion de datos

def newCategory(name, id):
    """
    Esta estructura almancena las categories utilizadas para marcar videos.
    """

    category={}
    category["name"]=name
    category["category_id"]=id
    return category


def newVideoCategory(catalog_category, video):
    """
    Esta estructura crea una relación entre un tag y
    los libros """

    category_id = video["category_id"]

    for category_dict in lt.iterator(catalog_category):
        
        if category_dict["category_id"] == category_id:

            category_name = category_dict["name"]

    return  category_name


# Funciones para creacion de datos


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) < float(video2['views']))


# Funciones de ordenamiento

def sortVideos(catalog, size, sorting_algorithm):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()

    if sorting_algorithm == "SHELL":
        sorted_list = shellsort.sort(sub_list, cmpVideosByViews)

    elif sorting_algorithm == "SELECTION":
        sorted_list = selectionsort.sort(sub_list, cmpVideosByViews)

    elif sorting_algorithm == "INSERTION":
        sorted_list = insertionsort.sort(sub_list, cmpVideosByViews)

    elif sorting_algorithm == "MERGE":
        sorted_list = mergesort.sort(sub_list, cmpVideosByViews)

    elif sorting_algorithm == "QUICK":
        sorted_list = quicksort.sort(sub_list, cmpVideosByViews)


    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
