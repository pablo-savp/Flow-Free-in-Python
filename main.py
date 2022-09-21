import numpy as np
import random
from collections import defaultdict

def crear_tablero(dimension):

    tablero = np.zeros((dimension, dimension), dtype=int)
    color = 1
    listaOrigenes = []

    if dimension > 7:
        colores = 11
        rang = 6
    else:
        colores = 9
        rang = 5

    for i in range(1, colores):
        posicionVacia = True
        while posicionVacia:
            x = random.randint(0, dimension-1)
            y = random.randint(0, dimension-1)

            if tablero[x, y] == 0:
                listaOrigenes.append(x)
                listaOrigenes.append(y)
                tablero[x, y] = color
                posicionVacia = False

        if i % 2 == 0:
            color+=1

    origenes = defaultdict(list)
    recorrer= 0

    for i in range(1, rang):
        for j in range(recorrer, 4+recorrer):
            origenes[i].append(listaOrigenes[j])
            recorrer=j+1

    return tablero, origenes

def es_origen(color, dimension, tablero, x, y):

    origenes = tablero[1]
    #print(f"Color en origen {color}")
    if (x >= dimension or x < 0) or (y >= dimension or y < 0):
        pass
    else:
        if (x == origenes[color][0] and y == origenes[color][1]) or (x == origenes[color][2] and y == origenes[color][3]):
            #print("--Es origen--")
            return True
        else:
            #print("--No es origen--")
            return False

def borrar_color(color, dimension, tablero):

    for j in range(0, dimension-1):
        for i in range(0, dimension - 1):
            if tablero[0][i][j] == color and not es_origen(color, dimension, tablero, i, j):
                tablero[0][i][j] = 0
    return tablero


def moverse(coloresCompletados, dimension, tablero, x, y, casillas, direccion, turno,  listaCompletados):

    color = tablero[0][x,y]
    print(listaCompletados)
    if color == 0:
        print("No se puede iniciar un movimiento desde una celda vacia\n")
        print(tablero[0])
        return 0

    if es_origen(color, dimension, tablero, x, y):
        origen = True
    else:
        origen = False

    if origen == True and color in listaCompletados:
        print("Entre a borrar color")
        borrar_color(color, dimension, tablero)
        listaCompletados.remove(color)
        print(tablero[0])
        print(listaCompletados)
        return -1

    if direccion == 'arriba':

        for i in range(1,casillas+1):

            valido = validar_movimiento(dimension, tablero, x-i, y, color, i)
            if valido == True:

                tablero[0][x-i,y] = color
                if origen == True and i==1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x-i, y, tablero)

                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print("ENTRE A COSO")
                    print(listaCompletados)
                    return coloresCompletados

            else:
                return 0

        return coloresCompletados

    elif direccion == 'abajo':

        for i in range(1,casillas+1):

            valido = validar_movimiento(dimension, tablero, x + i, y, color, i)

            if valido == True:

                tablero[0][x+i,y] = color
                if origen == True and i==1: #ESTO NO VALIDA LA POSIBILIDAD DE QUE EL COLOR ESTE A 1 MOVIMIENTO DE COMPLETARSE DESDE EL PRIMER MOV
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x+i, y , tablero)
                    print("entre a else")

                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print("ENTRE A COSO")
                    print(listaCompletados)
                    return coloresCompletados
            else:
                return 0

        return coloresCompletados

    elif direccion == 'izquierda':
        for i in range(1,casillas+1):

            valido = validar_movimiento(dimension, tablero, x , y-i, color, i)
            print(tablero[0])

            if valido == True:

                tablero[0][x,y-i] = color
                if origen == True and i == 1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x, y-i, tablero)
                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print("ENTRE A COSO")
                    print(listaCompletados)
                    return coloresCompletados

            else:
                return 0

        return coloresCompletados

    elif direccion == 'derecha':

        for i in range(1,casillas+1):

            valido = validar_movimiento(dimension, tablero, x, y + i, color, i)
            print(tablero[0])

            if valido == True:

                tablero[0][x, y + i] = color
                if origen == True and i == 1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x, y+i, tablero)

                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print("ENTRE A COSO")
                    print(listaCompletados)
                    return coloresCompletados
            else:
                return 0

        return coloresCompletados


def validar_movimiento(dimension, tablero, x, y, color, movimiento):

    print(f"Movimiento: {movimiento}\n")
    movimientoValido = True

    if (x >= dimension or x < 0) or (y >= dimension or y < 0):
        print(f"Las coordenadas del movimiento {movimiento} se salen del tablero, movimiento invalido")
        movimientoValido = False

    elif tablero[0][x,y] != 0:
        print(f"El movimiento {movimiento} no es posible ya que esa casilla se encuentra ocupada")
        movimientoValido = False

    return movimientoValido

def color_conectado(dimension, color, x, y, tablero):

    print("COLOR ACTUAL")
    print(color)

    if es_origen(color, dimension, tablero, x-1, y):
        print("ENTRO ARRIBA")
        if x-1 < 0:
            pass
        elif tablero[0][x-1,y] == color:
            print(f"COLOR {color} CONECTADO")
            return 1

    elif es_origen(color, dimension, tablero, x+1, y):
        print("ENTRO ABAJO")

        if x + 1 >= dimension:
            pass
        elif tablero[0][x+1,y] == color:
            print(f"COLOR {color} CONECTADO")
            return 1

    elif es_origen(color, dimension, tablero, x, y-1):
        print("ENTRO IZQ")
        if y-1 < 0:
            pass
        elif tablero[0][x, y-1] == color:
            print(f"COLOR {color} CONECTADO")
            return 1

    elif es_origen(color, dimension, tablero, x, y+1):
        print("ENTRO ABAJO")
        if y + 1 >= dimension:
            pass
        elif tablero[0][x, y + 1] == color:
            print(f"COLOR {color} CONECTADO")
            return 1
    else:
        print("COLOR NO CONECTADO AUN")
        return 0


def ganar(turno):

    print("==============================================")
    print(f"Felicitaciones, ha conectado todos los colores en {turno} turnos.")
    print("==============================================")
    print("\n")

    return True

#--------------------------------------------------------------------------------------------------------
#SI LA PERSONA VUELVE A ELEGIR ORIGEN DE UN COLOR, SE RESETEA TODA LA LINEA Y SI ESA LINEA YA ESTABA
#COMPLETADA ENTONCES SE HACE -1 AL CONTADOR DE COLORES CONECTADOS
#VALIDAR QUE LUEGO DE CONECTAR UN COLOR, NO PUEDA SEGUIR DIBUJANDO EN DADO CASO QUE ME DEN UNA LINEA QUE SOBREPASA EL COLOR
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def validar_dimensiones():

    while True:
        try:
            dimension = input("Ingresar la dimension del tablero deseado para jugar (5x5, 6x6, 7x7, 8x8, 9x9, 10x10): ")
            dimension = int(dimension)
        except:
            print("Por favor ingresar digitos y no letras, el digito debe indicar la dimension deseada para jugar\n")
        else:
            if isinstance(dimension, int) and dimension > 0:
                print("entre")
                return dimension
            else:
                print("Por favor ingresar dimensiones posibles, el digito debe indicar la dimension deseada para jugar\n")

    return dimension

def validar_coordenadas(dimension, turno, tablero):

    while True:
        try:
            if turno == 1:
                print("Ingresar coordenadas de origen (debe ser el origen de un color) ")
            else:
                print("Ingresar coordenadas de origen (puede ser un color o continuar una linea)")

            x = int(input("Coordenada x: "))
            y = int(input("Coordenada y: "))
        except:
            print("Las coordenadas deben ser digitos\n")
        else:
            if (x >= dimension or x < 0) or (y >= dimension or y < 0):
                print(f"Las coordenadas deben estar dentro del rango posible del tablero. Dimension del tablero: {dimension}")
            else:
                return x,y

def validar_casillas(tablero, dimension):

    while True:
        try:
            casillas = int(input("Cantidad de casillas que desea moverse: "))
        except:
            print("La cantidad casillas deben ser digitos\n")
        else:
            if casillas > dimension or casillas <= 0:
                print(f"La cantidad de casillas no puede ser mayor a la dimension del tablero ni menor o igual a 0{dimension}\n")
                print(tablero[0])
            else:
                return casillas

def validar_direccion(direccionesPosibles):

    while True:
        try:
            print("--Direcciones posibles: arriba, abajo, izquierda, derecha--")
            direccion = str(input("Dirección (Solo puede moverse en una direccion por movimiento, en el siguiente movimiento puede cambiar direccion): "))

        except:
            print("La direccion debe ser un texto\n")
        else:
            if direccion.isnumeric():
                print("La direccion debe ser un texto\n")
            elif direccion not in direccionesPosibles:
                print("La direccion debe ser una direccion posible\n")
            else:
                return direccion

if __name__ == '__main__':

    Jugar = True
    direccionesPosibles = ["arriba", "abajo", "derecha", "izquierda"]

    while Jugar:

        print("=============================================")
        print("          Bienvenido a Flow Free             ")
        print("=============================================")

        Ganar = False
        turno = 0
        dimension = validar_dimensiones()
        tablero = crear_tablero(dimension)
        print(tablero[0])
        print(tablero[1])
        listaCompletados = []
        coloresCompletados = 0
        contarcompletados = 0

        while Ganar == False:

            turno+=1
            coordenadas = validar_coordenadas(dimension, turno, tablero)
            x = coordenadas[0]
            y = coordenadas[1]
            casillas = validar_casillas(tablero, dimension)
            direccion = validar_direccion(direccionesPosibles)

            contarcompletados += moverse(coloresCompletados, dimension, tablero, x, y, casillas, direccion, turno, listaCompletados)
            print(f"COLORES COMPLETADOS: {contarcompletados}")

            if (contarcompletados == 4 and dimension<7) or (contarcompletados == 5 and dimension>=7):
                Ganar = ganar(turno)





