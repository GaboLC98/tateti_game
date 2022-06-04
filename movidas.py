import time
from tablas import *

def movida():#FUNCION DESPUES DE CADA MOVIDA
    print("")
    time.sleep(1)
    print("Buena movida!")
    time.sleep(1)
    print("\nTABLERO:")
    print(tablero[6],tablero[7],tablero[8])
    print(tablero[3],tablero[4],tablero[5])
    print(tablero[0],tablero[1],tablero[2])
    print("")
def movx():
    time.sleep(1)
    print("\nMUEVEN LAS X")
    movx=int(input("¿Donde desea colocar la ficha?\nPosicion nro -----> "))
    tablero[movx]="[X]"
def movo():
    time.sleep(1)
    print("\nMUEVEN LAS O")
    movo=int(input("¿Donde desea colocar la ficha?\nPosicion nro -----> "))
    tablero[movo]="[O]"