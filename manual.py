import Sokoban
arch = "a"
board = Sokoban.Board(arch)
board.Print()
while (True):
    mov = input()
    board.mover(mov)
    print("==========================================")
    board.Print()