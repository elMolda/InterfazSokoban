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
        if (direccion=='W'):
			#Avanzar Arriba
            if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] == const.LIBRE and self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] == const.JUGADOR): # Si la siguiente casilla esta libre
                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADOR
                return self.Data
            else:
                if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] == const.CAJA and self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] == const.JUGADOR): # Si en la siguiente casilla hay una caja
                    if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.LIBRE): # Si depues de la caja hay vacio
                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADOR
                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJA
                        return self.Data
                    else:
                        if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.META): # Si despues de la caja hay una meta
                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADOR
                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJAM
                            return self.Data
                else:
                    if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] == const.CAJAM): #Recordar Jugador sobre meta
                        if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.LIBRE): #META CAJA LIBRE
                            if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
								#JUGADOR MET
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJA
                                return self.Data
                            else: #LIBRE ACT
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJA
                                return self.Data
                        else:
                            if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.META ):
                                if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
									#JUGADOR MET
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJAM
                                    return self.Data
                                else: #LIBRE ACT
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJAM
                                    return self.Data
                            else:
                                return False
        else:
            if (direccion=='A'):
                #Avanzar Izquierda
                if ( self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si la siguiente casilla esta libre
                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                    self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ]] = const.JUGADOR
                    return self.Data
                else:
                    if ( self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] == const.CAJA): # Si en la siguiente casilla hay una caja
                        if ( self.Data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si depues de la caja hay vacio
                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                            self.Data[ self.playerpos[ 0 ] - 1][ self.playerpos[ 1 ] ] = const.JUGADOR
                            self.Data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] = const.CAJA
                            return self.Data
                        else:
                            if ( self.Data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] == const.META): # Si despues de la caja hay una meta
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                self.Data[ self.playerpos[ 0 ] - 1][ self.playerpos[ 1 ] ] = const.JUGADOR
                                self.Data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] = const.CAJAM
                                return self.Data
                    else:
                        if ( self.Data[ self.playerpos[ 0 ] - 1][ self.playerpos[ 1 ] ] == const.CAJAM): #Recordar Jugador sobre meta
                            if ( self.Data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] == const.LIBRE): #META CAJA LIBRE
                                if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
									#JUGADOR MET
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                    self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                    self.Data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] = const.CAJA
                                    return self.Data
                                else: #LIBRE ACT
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                    self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                    self.Data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] = const.CAJA
                                    return self.Data
                            else:
                                if ( self.Data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] == const.META ):
                                    if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
                                        #JUGADOR MET
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                        self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                        self.Data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] = const.CAJAM
                                        return self.Data
                                    else: #LIBRE ACT
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                        self.Data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                        self.Data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] = const.CAJAM
                                        return self.Data
                                else:
                                    return False
            else:
                if (direccion=='S'):
					#Avanzar Abajo
                    if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] == const.LIBRE): # Si la siguiente casilla esta libre
                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADOR
                        return self.Data
                    else:
                        if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] == const.CAJA): # Si en la siguiente casilla hay una caja
                            if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.LIBRE): # Si depues de la caja hay vacio
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADOR
                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJA
                                return self.Data
                            else:
                                if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.META): # Si despues de la caja hay una meta
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADOR
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJAM
                                    return self.Data
                        else:
                            if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] == const.CAJAM): #Recordar Jugador sobre meta
                                if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.LIBRE): #META CAJA LIBRE
                                    if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
										#JUGADOR MET
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJA
                                        return self.Data
										
                                    else: #LIBRE ACT
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJA
                                        return self.Data
                                else:
                                    if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.META ):
                                        if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
											#JUGADOR MET
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJAM
                                            return self.Data
                                        else: #LIBRE ACT
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJAM
                                            return self.Data
                                    else:
                                        return False
                else:
                    if (direccion=='D'):
						#Avanzar Derecha
                        if ( self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si la siguiente casilla esta libre
                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                            self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ]] = const.JUGADOR
                            return self.Data
                        else:
                            if ( self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] == const.CAJA): # Si en la siguiente casilla hay una caja
                                if ( self.Data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si depues de la caja hay vacio
                                    self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                    self.Data[ self.playerpos[ 0 ] + 1][ self.playerpos[ 1 ] ] = const.JUGADOR
                                    self.Data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] = const.CAJA
                                    return self.Data
                                else:
                                    if ( self.Data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] == const.META): # Si despues de la caja hay una meta
                                        self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                        self.Data[ self.playerpos[ 0 ] + 1][ self.playerpos[ 1 ] ] = const.JUGADOR
                                        self.Data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] = const.CAJAM
                                        return self.Data
                            else:
                                if ( self.Data[ self.playerpos[ 0 ] + 1][ self.playerpos[ 1 ] ] == const.CAJAM): #Recordar Jugador sobre meta
                                    if ( self.Data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] == const.LIBRE): #META CAJA LIBRE
                                        if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
											#JUGADOR MET
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                            self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                            self.Data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] = const.CAJA
                                            return self.Data
                                        else: #LIBRE ACT
                                            self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                            self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                            self.Data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] = const.CAJA
                                            return self.Data
                                    else:
                                        if ( self.Data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] == const.META ):
                                            if ( self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
												#JUGADOR MET
                                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
                                                self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                                self.Data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] = const.CAJAM
                                                return self.Data
                                            else: #LIBRE ACT
                                                self.Data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
                                                self.Data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
                                                self.Data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] = const.CAJAM
                                                return self.Data
                                        else:
                                            return False
                    else:
                        return self.playerpos
    
    def Print (self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.Data]))

    
