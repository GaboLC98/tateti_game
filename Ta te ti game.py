import time
print("\nTA TE TI GAME!\n")
tablero=["[₀]","[₁]","[₂]","[₃]","[₄]","[₅]","[₆]","[₇]","[₈]",]#TABLERO PRINCIPAL DONDE SE HARAN LOS CAMBIOS
tablero_prueba=["[X]","[₁]","[₂]","[₃]","[O]","[₅]","[₆]","[₇]","[₈]",]#TABLERO SECUNDARIO PARA MODIFICAR PARA INSTRUCCIONES
tablero_prueba1=["[X]","[X]","[X]","[O]","[O]","[₅]","[₆]","[O]","[₈]",]#TABLERO SECUNDARIO 2 PARA MODIFICAR PARA INSTRUCCIONES
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
def tabla():#TABLA QUE SE MODIFICA EN EL JUEGO
    print(tablero[6],tablero[7],tablero[8])
    print(tablero[3],tablero[4],tablero[5])
    print(tablero[0],tablero[1],tablero[2])
def tabla1():#TABLA DE PRUEBA EN INSTRUCCIONES
    print(tablero_prueba[6],tablero_prueba[7],tablero_prueba[8])
    print(tablero_prueba[3],tablero_prueba[4],tablero_prueba[5])
    print(tablero_prueba[0],tablero_prueba[1],tablero_prueba[2])
def tabla2():#TABLA DE PRUEBA 2 EN INSTRUCCIONES
    print(tablero_prueba1[6],tablero_prueba1[7],tablero_prueba1[8])
    print(tablero_prueba1[3],tablero_prueba1[4],tablero_prueba1[5])
    print(tablero_prueba1[0],tablero_prueba1[1],tablero_prueba1[2])
def init():#COMIENZA LA PARTIDA
    menu=int(input("Menu principal:\nPresione...\n1- Instrucciones\n2- Comenzar juego\n3- Salir\n----------> "))
    while menu:
        if menu==1:#INSTRUCCIONES
            print("Instrucciones:")
            time.sleep(1)
            print("El tablero esta compuesto por 3 filas donde se deberan poner las fichas.")
            time.sleep(4)
            print("Cada lugar tiene un nro el cual indica la posicion de dicho espacio\n")
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
            time.sleep(1)
            movx()
            movida()
            movo
            movida() 
            movx()
            movida()
            movo
            movida()
            movx()
            movida()
            corroborar()
            movo
            movida()
            corroborar()
            movx()
            movida()
            corroborar()
            movo
            movida()
            movx()
            movida()
            print("\n ES UN EMPATE!")
            init()
        elif menu==3:#TERMINA
            print("Hasta luego!")
            break
        else:#VUELVE A PEDIR DATOS
            print("\nOpcion incorrecta, vuelva a intentarlo...")
            init()
init()
