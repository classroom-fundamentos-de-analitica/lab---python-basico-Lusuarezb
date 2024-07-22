"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
# Lectura del archivo
import csv
archivo = []
with open("data.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter= "	")  
        for row in csvreader:
            archivo.append(row)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    counter = 0
    for linea in archivo:
        counter += int(linea[1])
    return counter


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    contador = {}
    for linea in archivo:
        key = linea[0]
        contador[key] = contador.get(key, 0) + 1
    return sorted(list(contador.items()))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    contador = {}
    for linea in archivo:
        key, valor = linea[0], int(linea[1])
        contador[key] = contador.get(key, 0) + valor
    return sorted(list(contador.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    contador = {}
    for linea in archivo:
        fecha = linea[2].split("-")
        key = fecha[1]
        contador[key] = contador.get(key, 0) + 1
    return sorted(list(contador.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    contador = {}
    for linea in archivo:
        key, valor = linea[0], int(linea[1])
        contador[key] = (max(valor, contador.get(key, (valor, valor))[0]), min(valor, contador.get(key, (valor, valor))[1]))
    auxiliar = [(tupla[0], tupla[1][0], tupla[1][1]) for tupla in list(contador.items())]
    return sorted(auxiliar)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    contador = {}
    for linea in archivo:
        division = linea[4].split(",")
        for termino in division:
            key,valor = termino.split(":")
            valor = int(valor)
            contador[key] = (min(valor, contador.get(key, (valor, valor))[0]), max(valor, contador.get(key, (valor, valor))[1]))
    auxiliar = [(tupla[0], tupla[1][0], tupla[1][1]) for tupla in list(contador.items())]
    return sorted(auxiliar)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    contador = {}
    for linea in archivo:
        key, valor = int(linea[1]), linea[0]
        contador[key] = contador.get(key, []) + [valor]
    return sorted(list(contador.items()))


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    contador = {}
    for linea in archivo:
        llave, valor = int(linea[1]), linea[0]
        if (valor not in contador.get(llave, [])):
            contador[llave] = sorted(contador.get(llave, []) + [valor])
    return sorted(list(contador.items()))


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    contador = {}
    for linea in archivo:
        division = linea[4].split(",")
        for termino in division:
            llave = termino.split(":")[0]
            contador[llave] = contador.get(llave, 0) + 1

    diccionario = {}
    for key in sorted(contador.keys()):
        diccionario[key] = contador[key]
    
    return diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    contador = []
    for linea in archivo:
        llave, valor1, valor2 = linea[0], len(linea[3].split(",")), len(linea[4].split(","))
        contador.append((llave,valor1, valor2))
    return contador


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    contador = {}
    for linea in archivo:
        llaves, valor = linea[3].split(","), int(linea[1])
        for llave in llaves:
            contador[llave] = contador.get(llave, 0) + valor
    
    diccionario = {}
    for key in sorted(contador.keys()):
        diccionario[key] = contador[key]
        
    return diccionario

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    contador = {}
    for linea in archivo:
        llave, valores = linea[0], linea[4].split(",")
        for valor in valores:
            numero = int(valor.split(":")[1])
            contador[llave] = contador.get(llave, 0) + numero

    diccionario = {}
    for key in sorted(contador.keys()):
        diccionario[key] = contador[key]
        
    return diccionario
