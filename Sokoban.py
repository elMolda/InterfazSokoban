import const
class Board:
     ## ---------------------------------------------------------------------
    Data = [[]]
    Width = 0
    Height = 0


    ## ---------------------------------------------------------------------

    def __init__( self, arch ):
         print(const.CAJA)
         cont = 0
         with open('tablero.txt') as f:
            lines = f.readlines()
            for line in lines:
                if(cont == 0):
                    print("WIDTH ES: ",line)
                    self.Width = line
                    cont +=1
                elif(cont == 1):
                    self.Height = line
                    cont +=1
                else:
                    self.Data[cont-2] = line
                    cont+=1
                print("==============")
                print(line)
         f.close()
         print("Width: ",self.Width)
         print("Height: ",self.Height)
         print("tabla")
         print(self.Data)

    def mover (self,direccion):
        print("B")
    
    def Print (self):
        print("c")
    
