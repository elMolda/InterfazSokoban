import const
class Board:
     ## ---------------------------------------------------------------------
    Data = [[]]
    Width = 0
    Height = 0
    playerpos = [0,0]

    ## ---------------------------------------------------------------------

    def __init__( self, arch ):
         print(const.CAJA)
         with open('tablero.txt') as f:
            lines = f.readlines()
            self.Width = int(lines[0])
            self.Height = int(lines[1])
            self.llenarMatriz(lines)    
         f.close()
         print("Width: ",self.Width)
         print("Height: ",self.Height)
         print("jugador: ", self.playerpos)
         print("tabla")
         print(self.Data)

    def llenarMatriz(self,lines):
        print("W: ",self.Width, "H: ",self.Height)

        self.Data = [ [ (0) for j in range(self.Height)] for i in range(self.Width) ]
        for i in range (2,self.Height+2):
            for j in range (0,self.Width):
                self.Data[i-2][j] = lines[i][j]
                if(self.Data[i-2][j] == const.JUGADOR or self.Data[i-2][j] == const.JUGADORM):
                    self.playerpos = [i-2,j]

    def mover (self,direccion):
        print("B")
    
    def Print (self):
        print("c")
    
