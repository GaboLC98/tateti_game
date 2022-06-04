import time
from movidas import *
from tablas import *

def corroborar():#VERIFICO SI HAY UN GANADOR
    if "X" in tablero[0] and "X" in tablero[1] and "X" in tablero[2] or "X" in tablero[0] and "X" in tablero[3] and "X" in tablero[6] or "X" in tablero[1] and "X" in tablero[4] and "X" in tablero[7] or "X" in tablero[2] and "X" in tablero[5] and "X" in tablero[8] or "X" in tablero[0] and "X" in tablero[4] and "X" in tablero[8] or "X" in tablero[6] and "X" in tablero[4] and "X" in tablero[2] or "X" in tablero[3] and "X" in tablero[4] and "X" in tablero[5] or "X" in tablero[6] and "X" in tablero[7] and "X" in tablero[8]:
        print("\n\nGANAN LAS X!\n\n")
        time.sleep(2)
        init()
    elif "O" in tablero[0] and "O" in tablero[1] and "O" in tablero[2] or "O" in tablero[0] and "O" in tablero[3] and "O" in tablero[6] or "O" in tablero[1] and "O" in tablero[4] and "O" in tablero[7] or "O" in tablero[2] and "O" in tablero[5] and "O" in tablero[8] or "O" in tablero[0] and "O" in tablero[4] and "O" in tablero[8] or "O" in tablero[6] and "O" in tablero[4] and "O" in tablero[2] or "O" in tablero[3] and "O" in tablero[4] and "O" in tablero[5] or "O" in tablero[6] and "O" in tablero[7] and "O" in tablero[8]:
        print("\n\nGANAN LAS O!\n\n")
        time.sleep(2)
        init()
    else:
        return ""

def init():#COMIENZA LA PARTIDA
    menu=int(input("Menu principal:\nPresione...\n1- Instrucciones\n2- Comenzar juego\n3- Salir\n----------> "))
    while menu:
        if menu==1:#INSTRUCCIONES
            print("Instrucciones:")
            time.sleep(1)
            print("El tablero esta compuesto por 3 filas donde se deberan poner las fichas.")
            time.sleep(4)
            print("Cada lugar tiene un nro el cual indica la posicion de dicho espacio")
            time.sleep(4)
            tabla()
            print("")
            time.sleep(2)
            print("Si este espacio se encuentra ocupado aparecera una X o una O:\n\nTABLERO ocupado")
            time.sleep(2)
            tabla1()
            time.sleep(1)
            print("Como se puede observar el nro 0 y 4 se encuentran ocupados por la X y la O respectivamente")
            time.sleep(4)
            print("El primero en completar una fila gana la partida")
            time.sleep(1)
            print("\nTABLERO con ganador:")
            tabla2()
            time.sleep(1)
            print("EL GANADOR SON LAS X!\n")
            init()
        elif menu ==2:#PARTIDA PvP
            tabla()
            for x in range(4):
                movx()
                movida()
                corroborar()
                movo()
                movida()
                corroborar()
            movx()
            movida()
            corroborar()
            print("\n ES UN EMPATE!")
            init()
        elif menu==3:#TERMINA
            print("Hasta luego!")
            break
        else:#VUELVE A PEDIR DATOS
            print("\nOpcion incorrecta, vuelva a intentarlo...")
            init()

print("\nTA TE TI GAME!\n")

init()
