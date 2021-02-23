﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initCatalog(list_type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(list_type)
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadCategories(catalog)
    loadVideos(catalog)





def loadCategories(catalog):
    """
    Carga todas los categories del archivo y las agrega a la lista de categories
    """

    category_file=cf.data_dir +"category-id.csv"
    input_file=csv.DictReader(open(category_file, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)



def loadVideos(catalog):
    """
    Carga los videos del archivo CSV.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


# Funciones de ordenamiento

def sortVideos(catalog, size, sorting_algorithm):
    """
    Ordena los videos por número de views
    """
    return model.sortVideos(catalog, size, sorting_algorithm)


# Funciones de consulta sobre el catálogo
