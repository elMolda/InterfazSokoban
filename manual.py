import Sokoban
arch = "a"
board = Sokoban.Board(arch)
board.Print()
i = 0
gano = False
while (not gano):
    mov = input()
    board.movimientos(mov)
    print("==============================================================================================================================")
    board.Print()
    gano = board.estadodeljugador()
print("GAME OVER")