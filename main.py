import numpy as np
import random
from collections import defaultdict
from numpy import reshape


def crear_tablero(dimension):

    tablero = np.zeros((dimension, dimension), dtype=int)
    color = 1
    listaOrigenes = []
    positionCheck = []
    colores = 9

    for i in range(1, colores):
        posicionVacia = True
        while posicionVacia:
            x = random.randint(0, dimension-1)
            if i % 2 == 0:
                if dimension > 5:
                    while True:
                        if x == positionCheck[0] or x + 1 == positionCheck[0] or x + 2 == positionCheck[0] or x - 1 == positionCheck[0] or x - 2 == positionCheck[0]:
                            x = random.randint(0, dimension - 1)
                            y = random.randint(0, dimension - 1)
                        else:
                            break
                else:
                    while True:
                        if x == positionCheck[0] or x + 1 == positionCheck[0] or x-1 == positionCheck[0]:
                            x = random.randint(0, dimension - 1)
                            y = random.randint(0, dimension - 1)
                            if (y + 1 != positionCheck[1] or y - 1 != positionCheck[1]) and y != positionCheck[1] and x!=positionCheck[0]:
                                y = y + 2
                                break
                        else:
                            break

            else:
                y = random.randint(0, dimension - 1)

            if tablero[x, y] == 0:
                positionCheck.append(x)
                positionCheck.append(y)
                listaOrigenes.append(x)
                listaOrigenes.append(y)
                tablero[x, y] = color
                posicionVacia = False


        if i % 2 == 0:
            color+=1
            positionCheck = []

    origenes = defaultdict(list)
    recorrer= 0

    for i in range(1, 5):
        for j in range(recorrer, 4+recorrer):
            origenes[i].append(listaOrigenes[j])
            recorrer=j+1

    return tablero, origenes

def es_origen(color, dimension, tablero, x, y):

    origenes = tablero[1]

    if (x >= dimension or x < 0) or (y >= dimension or y < 0):
        pass
    else:
        if (x == origenes[color][0] and y == origenes[color][1]) or (x == origenes[color][2] and y == origenes[color][3]):
            return True

        else:
            return False

def borrar_color(color, dimension, tablero):

    for j in range(0, dimension-1):
        for i in range(0, dimension - 1):
            if tablero[0][i][j] == color and not es_origen(color, dimension, tablero, i, j):
                tablero[0][i][j] = 0
    return tablero

def backtracking_coordenadas(color, dimension, tablero, x, y, mov_color1, mov_color2, mov_color3, mov_color4):
    i = 0
    pos = 0

    for j in range(0, dimension*3):

        if color == 1:
            if mov_color1[i,j] == x and mov_color1[i+1,j] == y:
                print("Movimiento ya existe, vamos a borrar movimientos posteriores")
                pos = j
                for c in range(pos + 1, (dimension * 3)):
                    tabx = mov_color1[i, c]
                    taby = mov_color1[i + 1, c]
                    mov_color1[i, c] = -1
                    mov_color1[i + 1, c] = -1
                    tablero[0][tabx, taby] = 0
                print(mov_color1)
                break

        if color == 2:
            if mov_color2[i, j] == x and mov_color2[i + 1, j] == y:
                print("Movimiento ya existe, vamos a borrar movimientos posteriores")
                pos = j
                for c in range(pos + 1, (dimension * 3)):
                    tabx = mov_color2[i, c]
                    taby = mov_color2[i + 1, c]
                    mov_color2[i, c] = -1
                    mov_color2[i + 1, c] = -1
                    tablero[0][tabx, taby] = 0
                print(f"Lista de movimientos del color {color}")
                print(mov_color2)
                break

        if color == 3:
            if mov_color3[i, j] == x and mov_color3[i + 1, j] == y:
                print("Movimiento ya existe, vamos a borrar movimientos posteriores")
                pos = j
                for c in range(pos + 1, (dimension * 3)):
                    tabx = mov_color3[i, c]
                    taby = mov_color3[i + 1, c]
                    mov_color3[i, c] = -1
                    mov_color3[i + 1, c] = -1
                    tablero[0][tabx, taby] = 0

                print(f"Lista de movimientos del color {color}")
                print(mov_color3)
                break

        if color == 4:
            if mov_color4[i, j] == x and mov_color4[i + 1, j] == y:
                print("Movimiento ya existe, vamos a borrar movimientos posteriores")
                pos = j
                for c in range(pos + 1, (dimension * 3)):
                    tabx = mov_color4[i, c]
                    taby = mov_color4[i + 1, c]
                    mov_color4[i, c] = -1
                    mov_color4[i + 1, c] = -1
                    tablero[0][tabx, taby] = 0

                print(f"Lista de movimientos del color {color}")
                print(mov_color4)
                break

    return pos

def borrar_lista_movimientos(dimension, tablero, color,mov_color1, mov_color2, mov_color3, mov_color4):
    i = 0

    if color == 1:
        for j in range(0, dimension + 2):
            mov_color1[i, j] = -1
            mov_color1[i + 1, j] = -1

    elif color == 2:
        for j in range(0, dimension + 2):
            mov_color2[i, j] = -1
            mov_color2[i + 1, j] = -1

    elif color == 3:
        for j in range(0, dimension + 2):
            mov_color3[i, j] = -1
            mov_color3[i + 1, j] = -1

    elif color == 4:
        for j in range(0, dimension + 2):
            mov_color4[i, j] = -1
            mov_color4[i + 1, j] = -1

def moverse(coloresCompletados, dimension, tablero, x, y, casillas, direccion, listaCompletados,  mov_color1, mov_color2, mov_color3, mov_color4):

    valx = 0
    valy = 0
    color = tablero[0][x,y]
    print(f"Lista de colores completados: {listaCompletados}")

    if color == 0:
        print("No se puede iniciar un movimiento desde una celda vacia\n")
        print(tablero[0])
        return 0

    if es_origen(color, dimension, tablero, x, y):
        origen = True
    else:
        origen = False

    if origen == True and color in listaCompletados:

        borrar_color(color, dimension, tablero)
        borrar_lista_movimientos(dimension, tablero, color, mov_color1, mov_color2, mov_color3, mov_color4)
        listaCompletados.remove(color)
        print(tablero[0])
        print(f"--Color {color} borrado. Los movimientos estipulados de {casillas} casillas no contarán--")
        print(f"Colores completados luego de borrado: {listaCompletados}")
        return -1

    #Backtracking
    if color in listaCompletados:
        valy = backtracking_coordenadas(color, dimension, tablero, x, y, mov_color1, mov_color2, mov_color3, mov_color4)
        listaCompletados.remove(color)
        return -1
    else:
        valy = backtracking_coordenadas(color, dimension, tablero, x, y, mov_color1, mov_color2, mov_color3, mov_color4)

    if direccion == 'arriba':

        for i in range(1,casillas+1):
            valy = valy + 1

            valido = validar_movimiento(dimension, tablero, x-i, y, color, i)
            if valido == True:

                if color == 1:
                    if i <=1:
                        mov_color1[valx, valy - 1] = x
                        mov_color1[valx + 1, valy - 1] = y

                    mov_color1[valx, valy] = x - i
                    mov_color1[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color1)

                elif color == 2:
                    if i <= 1:
                        mov_color2[valx, valy - 1] = x
                        mov_color2[valx + 1, valy] = y

                    mov_color2[valx, valy - 1] = x - i
                    mov_color2[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color2)

                elif color == 3:
                    if i <= 1:
                        mov_color3[valx, valy - 1] = x
                        mov_color3[valx + 1, valy - 1] = y

                    mov_color3[valx, valy] = x - i
                    mov_color3[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color3)

                elif color == 4:
                    if i <= 1:
                        mov_color4[valx, valy - 1] = x
                        mov_color4[valx + 1, valy - 1] = y

                    mov_color4[valx, valy] = x - i
                    mov_color4[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color4)

                tablero[0][x-i,y] = color

                if origen == True and i==1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x-i, y, tablero)

                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print(listaCompletados)
                    return coloresCompletados

            else:
                return 0

        return coloresCompletados

    elif direccion == 'abajo':

        for i in range(1,casillas+1):

            valy = valy + 1
            valido = validar_movimiento(dimension, tablero, x + i, y, color, i)

            if valido == True:

                if color == 1:
                    if i <= 1:
                        mov_color1[valx, valy - 1] = x
                        mov_color1[valx + 1, valy - 1] = y

                    mov_color1[valx, valy] = x + i
                    mov_color1[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color1)

                elif color == 2:
                    if i <= 1:
                        mov_color2[valx, valy - 1] = x
                        mov_color2[valx + 1, valy - 1] = y

                    mov_color2[valx, valy] = x + i
                    mov_color2[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color2)

                elif color == 3:
                    if i <= 1:
                        mov_color3[valx, valy - 1] = x
                        mov_color3[valx + 1, valy - 1] = y

                    mov_color3[valx, valy] = x + i
                    mov_color3[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color3)

                elif color == 4:
                    if i <= 1:
                        mov_color4[valx, valy - 1] = x
                        mov_color4[valx + 1, valy - 1] = y

                    mov_color4[valx, valy] = x + i
                    mov_color4[valx + 1, valy] = y
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color4)

                tablero[0][x+i,y] = color

                if origen == True and i==1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x+i, y , tablero)

                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print(listaCompletados)
                    return coloresCompletados
            else:
                return 0

        return coloresCompletados

    elif direccion == 'izquierda':
        for i in range(1,casillas+1):

            valy = valy + 1
            valido = validar_movimiento(dimension, tablero, x , y-i, color, i)

            if valido == True:

                if color == 1:
                    if i <= 1:
                        mov_color1[valx, valy - 1] = x
                        mov_color1[valx + 1, valy - 1] = y

                    mov_color1[valx, valy] = x
                    mov_color1[valx + 1, valy] = y - i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color1)

                elif color == 2:
                    if i <= 1:
                        mov_color2[valx, valy - 1] = x
                        mov_color2[valx + 1, valy - 1] = y

                    mov_color2[valx, valy] = x
                    mov_color2[valx + 1, valy] = y - i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color2)

                elif color == 3:
                    if i <= 1:
                        mov_color3[valx, valy - 1] = x
                        mov_color3[valx + 1, valy - 1] = y

                    mov_color3[valx, valy] = x
                    mov_color3[valx + 1, valy] = y - i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color3)

                elif color == 4:
                    if i <= 1:
                        mov_color4[valx, valy - 1] = x
                        mov_color4[valx + 1, valy - 1] = y

                    mov_color4[valx, valy] = x
                    mov_color4[valx + 1, valy] = y - i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color4)

                tablero[0][x,y-i] = color
                if origen == True and i == 1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x, y-i, tablero)
                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
                    print(listaCompletados)
                    return coloresCompletados
            else:
                return 0

        return coloresCompletados

    elif direccion == 'derecha':

        for i in range(1,casillas+1):

            valy = valy + 1
            valido = validar_movimiento(dimension, tablero, x, y + i, color, i)

            if valido == True:

                if color == 1:
                    if i <= 1:
                        mov_color1[valx, valy - 1] = x
                        mov_color1[valx + 1, valy - 1] = y

                    mov_color1[valx, valy] = x
                    mov_color1[valx + 1, valy] = y + i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color1)

                elif color == 2:
                    if i <= 1:
                        mov_color2[valx, valy - 1] = x
                        mov_color2[valx + 1, valy - 1] = y

                    mov_color2[valx, valy] = x
                    mov_color2[valx + 1, valy] = y + i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color2)

                elif color == 3:
                    if i <= 1:
                        mov_color3[valx, valy - 1] = x
                        mov_color3[valx + 1, valy - 1] = y

                    mov_color3[valx, valy] = x
                    mov_color3[valx + 1, valy] = y + i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color3)

                elif color == 4:
                    if i <= 1:
                        mov_color4[valx, valy - 1] = x
                        mov_color4[valx + 1, valy - 1] = y

                    mov_color4[valx, valy] = x
                    mov_color4[valx + 1, valy] = y + i
                    print(f"Lista de movimientos del color {color}")
                    print(mov_color4)

                tablero[0][x, y + i] = color
                if origen == True and i == 1:
                    pass
                else:
                    coloresCompletados = color_conectado(dimension, color, x, y+i, tablero)

                print(tablero[0])

                if coloresCompletados == 1:
                    listaCompletados.append(color)
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


    if es_origen(color, dimension, tablero, x-1, y):
        if x-1 < 0:
            pass
        elif tablero[0][x-1,y] == color:
            print(f"--COLOR {color} CONECTADO--")
            return 1

    elif es_origen(color, dimension, tablero, x+1, y):
        if x + 1 >= dimension:
            pass
        elif tablero[0][x+1,y] == color:
            print(f"--COLOR {color} CONECTADO--")
            return 1

    elif es_origen(color, dimension, tablero, x, y-1):
        if y-1 < 0:
            pass
        elif tablero[0][x, y-1] == color:
            print(f"--COLOR {color} CONECTADO--")
            return 1

    elif es_origen(color, dimension, tablero, x, y+1):
        if y + 1 >= dimension:
            pass
        elif tablero[0][x, y + 1] == color:
            print(f"--COLOR {color} CONECTADO--")
            return 1
    else:
        print("--COLOR NO CONECTADO AUN--")
        return 0


def ganar(turno):

    print("==============================================")
    print(f"Felicitaciones, ha conectado todos los colores en {turno} turnos.")
    print("==============================================")
    print("\n")

    return True

def validar_dimensiones():

    while True:
        try:
            dimension = input("Ingresar la dimension del tablero deseado para jugar (5x5, 6x6, 7x7, 8x8, 9x9, 10x10, 11x11, 12x12, 13x13, 14x14): ")
            dimension = int(dimension)
        except:
            print("Por favor ingresar digitos y no letras, el digito debe indicar la dimension deseada para jugar\n")
        else:
            if isinstance(dimension, int) and dimension > 0 and dimension<=14:
                return dimension
            else:
                print("Por favor ingresar dimensiones posibles, el digito debe indicar la dimension deseada para jugar\n")

    return dimension

def validar_coordenadas(dimension, turno):

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
        listaCompletados = []
        coloresCompletados = 0
        contarcompletados = 0

        #Creacion de matrices para guardar movimientos
        mov_color1 = np.zeros((2, dimension*3), dtype=int)
        mov_color1 = reshape(mov_color1,(2,dimension*3))

        mov_color2 = np.zeros((2, dimension*3), dtype=int)
        mov_color2 = reshape(mov_color2, (2, dimension*3))

        mov_color3 = np.zeros((2, dimension*3), dtype=int)
        mov_color3 = reshape(mov_color3, (2, dimension*3))

        mov_color4 = np.zeros((2, dimension*3), dtype=int)
        mov_color4 = reshape(mov_color4, (2, dimension*3))

        while Ganar == False:

            turno+=1
            coordenadas = validar_coordenadas(dimension, turno)
            x = coordenadas[0]
            y = coordenadas[1]
            casillas = validar_casillas(tablero, dimension)
            direccion = validar_direccion(direccionesPosibles)

            contarcompletados += moverse(coloresCompletados, dimension, tablero, x, y, casillas, direccion, listaCompletados, mov_color1, mov_color2, mov_color3, mov_color4)
            print(f" Cantidad de colores completados: {contarcompletados}")
            print(tablero[0])

            if (contarcompletados == 4):
                Ganar = ganar(turno)