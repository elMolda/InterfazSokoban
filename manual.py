import Sokoban
#Rutas de niveles =============================
# Niveles/nivel1.txt
# Niveles/nivel2.txt
# Niveles/nivel3.txt

# Fin rutas ===================================
def jugadorManual():
    arch = "Niveles/nivel3.txt"
    board = Sokoban.Board(arch)
    board.Print()

    gano = False
    while (not gano):
        mov = input()
        board.movimientos(mov)
        print("============================================================================")
        board.Print()
        gano = board.estadoJugador()
    print("GAME OVER")

def jugadorAutomatico():
    arch = "Niveles/nivel3.txt"
    board = Sokoban.Board(arch)
    board.Print()
    board.jugadorAutomatico()


print ("==========MENU===========")
print ("1 ->  para jugador manual")
print ("2 -> para jugador automatico")
selection = input()
if(selection == "1"):
    jugadorManual()
elif (selection == "2"):
    jugadorAutomatico()
else:
    print("dato invalido")
    
