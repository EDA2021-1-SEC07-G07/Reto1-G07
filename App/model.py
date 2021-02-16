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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
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

    catalog["videos"]=lt.newList
    catalog["id_videos"]=lt.newList("ARRAY_LIST",None)
    catalog["categories"]=lt.newList("SINGLE_LINKED",None)
    catalog["videos_categories"]=lt.newList("SINGLE_LINKED")
    return catalog



# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtienen los id's de las categorías relacionadas al video
    categories_ids = video['category_id'].split(",")
    # Cada categoría, se crea en la lista de videos del catalogo, y se
    # crea un video en la lista de dicha categoría (apuntador al video)

    """
    for category_id in categories_ids:
        addVideoCategory(catalog, category_id.strip(), video)
    """
        
def addCategory(catalog, category):
    """
    Adiciona unas category a la lista de categories
    """

    t=newCategory(category["name"], category["category_id"])
    lt.addLast(catalog["categories"], t)

def addVideoCategory(catalog, video_category):

    t= newVideoCategory(video_category["category_id"], video_category["video_category_id"])
    lt.addLast(catalog["videos_categories"], t)


# Funciones para creacion de datos

def newCategory(name, id):
    """
    Esta estructura almancena las categories utilizados para marcar videos.
    """

    category={"name":"", " category_id": ""}
    category["name"]=name
    category["category_id"]=id
    return category


def newVideoCategory(category_id,video_category_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros """


    video_category={"category_id":category_id , "video_category_id": video_category_id}


    return video_category


# Funciones para creacion de datos


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento