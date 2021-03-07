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
from time import sleep

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
    try:
        if int(n_sample) > lt.size(catalog['videos']):
            
            print("El número de muestra ha superado el tamaño de la lista, se procederá con la cantidad máxima de videos dentro del catálogo: {}".format(lt.size(catalog['videos'])))

            sleep(5)
            n_sample = lt.size(catalog['videos'])-1
            
        return int(n_sample)
    except:
        return askSampleList(catalog)


def sortVideos(catalog, size, cmpFunction):
    """
    Organiza los videos mediante Merge Sort
    """
    return controller.sortVideos(catalog, size, cmpFunction)


def sortVideosByDays(catalog, size):
    """
    Organiza los videos mediante Merge Sort
    """
    return controller.sortVideosByDays(catalog, size)


def sortVideosByLikes(catalog,size):
    """
    Organiza los videos mediante Merge Sort
    """
    return controller.sortVideosByLikes(catalog, size)
    

# Pasar a model

def filterCategory(catalog):
    """Le pregunta al usuario bajo que categoría desea filtrar los algoritmos."""


    filter_category = input("Ingrese el nombre de la categoria con la que desea filtrar sus datos: ").lower()
    for category in lt.iterator(catalog['categories']):

        if filter_category == category["name"].strip().lower():

            return category["name"].strip()

    print("Este no es el nombre de una categoría existente. Intente de nuevo.")
    return filterCategory(catalog)


def filterCountry(catalog):
    """Le pregunta al usuario bajo que país desea filtrar los algoritmos."""

    filter_country = input("Ingrese el nombre del país con el que desea filtrar sus datos: ")

    if filter_country in lt.iterator(catalog["countries"]):
            
        return filter_country
    print("El país que has ingresado no ha sido identificado en la base de datos. Intentalo de nuevo.")
    return filterCountry(catalog)

def filterTag(catalog):
    """Le pregunta al usuario bajo que tag desea filtrar los algoritmos."""

    tag=input("Ingrese el Tag con el cual desea filtrar el video: ")
    filter_tag=controller.filterTag(catalog, tag)
    
    return filter_tag

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


def printResultsReq2(videos, dias):
    a = "title"
    b = "channel_title"
    c = "country"
    d = "Días"

    formato="|{}|{}|{}|{}|\n".format(a.center(10),b.center(10),c.center(10),d.center(10))+("-"*60)+"\n"
    texto="\n"+formato
        
   
    print("Los videos que más han permanecido en tendencias son: \n")

    for video in lt.iterator(videos):

        formato="|{}|{}|{}|{}|\n".format(video["title"].center(6),video["channel_title"].center(6), video["country"].center(6), dias.center(6))+("-"*60)+"\n"

        texto+=formato
    print(texto)


def printResultsReq4(list_videos, n_sample):
    for i in range(n_sample):
        a = "title"
        b= "channel_title"
        c = "publish_time"
        d="views"
        e = "likes"
        f = "dislikes"
        g="tags"

        names_categories=[a,b,c,d,e,f,g]
        video = lt.getElement(list_videos, i+1)[2]

        title=video[a]
        cannel_title=video[b]
        publish_time= video[c]
        views=video[d]
        likes= video[e]
        dislikes=video[f]
        tags=video[g]


        categories=[title,cannel_title,publish_time, views,likes,dislikes,tags]
        size_label_categories=[]
        for k in categories:
            try:
                size=len(k)
                size_label_categories.append(size)
            except:
                pass

        max_size=max(size_label_categories)
        print(max_size)
        upper="-"*(max_size+18)+"\n"
        text=upper+"|{}|\n".format(("VIDEO"+str(i)).center(max_size))+upper
       

        for j in range(len(categories)):
            a=str(names_categories[j]).center(15)
            b=str(categories[j]).center(max_size)
            value="|{}|{}|".format(a,b)
            text+=value
            text+=upper
        text+="\n"*5

        print(text)

def requerimiento_1(catalog):

    filter_category = filterCategory(catalog)
    filter_country = filterCountry(catalog)

    filtered_catalog = controller.filterCatalog(catalog = catalog, column_1 = "category_name", column_2 = "country", value_1 = filter_category, value_2 = filter_country)

    n_sample = askSampleList(filtered_catalog)

    top_views = sortVideos(filtered_catalog, lt.size(filtered_catalog["videos"]), "sortByViews")
    
    printResultsReq1(top_views[1], n_sample)

def requerimiento_2(catalog):

    filter_country = filterCountry(catalog)
    filtered_catalog = controller.filterCatalog(catalog = catalog, column_1 = "country", value_1 = filter_country)
        
    max_videos = lt.newList()

    unique_catalog = controller.initUniqueCatalog(filtered_catalog["videos"])

    top_days = sortVideos(unique_catalog, lt.size(unique_catalog), "sortByDays")


    first_video = lt.firstElement(top_days[1])

    max_days = first_video[0]

    pos = 1

    while lt.getElement(top_days[1], pos)[0] == max_days:

        lt.addLast(max_videos, lt.getElement(top_days[1], pos)[2])
        pos += 1

    printResultsReq2(max_videos, str(max_days))

def requerimiento_3(catalog):

    filter_category =" " + filterCategory(catalog)
    filtered_catalog = controller.filterCatalog(catalog = catalog, column_1 = "category_name", value_1 = filter_category)
        
    max_videos = lt.newList()
    unique_catalog = controller.initUniqueCatalog(filtered_catalog["videos"])
    top_days = sortVideos(unique_catalog, lt.size(unique_catalog), "sortByDays")


    first_video = lt.firstElement(top_days[1])
    max_days = first_video[0]
    pos = 1

    while lt.getElement(top_days[1], pos)[0] == max_days:

        lt.addLast(max_videos, lt.getElement(top_days[1], pos)[2])
        pos += 1

    printResultsReq2(max_videos, str(max_days))

def requerimiento_4(catalog):
    filter_country = filterCountry(catalog)                
    filtered_catalog = controller.filterCatalog(catalog = catalog, column_1 = "country", value_1 = filter_country)    
    
    filter_tag=filterTag(filtered_catalog)
    top_likes =sortVideos(filter_tag,lt.size(filter_tag["videos"]), "sortByLikes")
    unique_catalog = controller.initUniqueCatalog(top_likes[1])
    n_sample = askSampleList(filter_tag)

    printResultsReq4(unique_catalog, n_sample)




"""
Menu principal
"""
def MainMenu():

    try:
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
                requerimiento_1(catalog)


            elif int(inputs[0]) == 3:
                requerimiento_2(catalog)
            
            elif int(inputs[0])==4:
                requerimiento_3(catalog)

            elif int(inputs[0])==5:
                requerimiento_4(catalog)

            elif int(inputs[0]) == 0:


            
                sys.exit(0)

    except Exception:
        raise Exception
        print("No ha cargado la base de datos. Intentelo de nuevo.")
        MainMenu()
    sys.exit(0)


MainMenu()