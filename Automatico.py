import copy
import random

def jugar_auto(tablero):
    tabCpy = copy.copy(tablero)
    gano = -1
    movimientos = ["W","A","S","D"]
    print("====================================================================================")
    while (gano != 0 and gano != 2):
        mov = movimientos[random.randint(0,3)]
        tabCpy.movimientos(mov)
        tabCpy.Print()
        print("====================================================================================")
        gano = tabCpy.estadoJugador()
        if gano == 1:
            resJugada = gano
            while resJugada == 1:
                tabCpy.movimientos(mov)
                tabCpy.Print()
                print("====================================================================================")
                resJugada = tabCpy.estadoJugador()
    print("GAME OVER")
    if gano == 0:
        print("YOU LOSE")
    else:
        if gano == 2:
            print("YOU WIN")           
