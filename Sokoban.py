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
			if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] == const.LIBRE and self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] == const.JUGADOR): # Si la siguiente casilla esta libre
				self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
				self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADOR
				return self.data
			else:
				if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] == const.CAJA and self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] == const.JUGADOR): # Si en la siguiente casilla hay una caja
					if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.LIBRE): # Si depues de la caja hay vacio
						self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
						self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADOR
						self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJA
						return self.data
					else
						if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.META): # Si despues de la caja hay una meta
							self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
							self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADOR
							self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJAM
							return self.data
				else:
					if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] == const.CAJAM): #Recordar Jugador sobre meta
						if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.LIBRE): #META CAJA LIBRE
							if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
								#JUGADOR MET
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJA
								return self.data
							else: #LIBRE ACT
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJA
								return self.data
						else
							if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] == const.META ):
								if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
									#JUGADOR MET
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJAM
									return self.data
								else: #LIBRE ACT
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 1] = const.JUGADORM
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] + 2] = const.CAJAM
									return self.data
							else:
								return False
		else:
			if (direccion=='A'):
				#Avanzar Izquierda
				if ( self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si la siguiente casilla esta libre
					self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
					self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ]] = const.JUGADOR
					return self.data
				else:
					if ( self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] == const.CAJA): # Si en la siguiente casilla hay una caja
						if ( self.data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si depues de la caja hay vacio
							self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
							self.data[ self.playerpos[ 0 ] - 1][ self.playerpos[ 1 ] ] = const.JUGADOR
							self.data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] = const.CAJA
							return self.data
						else
							if ( self.data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] == const.META): # Si despues de la caja hay una meta
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
								self.data[ self.playerpos[ 0 ] - 1][ self.playerpos[ 1 ] ] = const.JUGADOR
								self.data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] = const.CAJAM
								return self.data
					else:
						if ( self.data[ self.playerpos[ 0 ] - 1][ self.playerpos[ 1 ] ] == const.CAJAM): #Recordar Jugador sobre meta
							if ( self.data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] == const.LIBRE): #META CAJA LIBRE
								if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
									#JUGADOR MET
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
									self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
									self.data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] = const.CAJA
									return self.data
								else: #LIBRE ACT
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
									self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
									self.data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] = const.CAJA
									return self.data
							else
								if ( self.data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] == const.META ):
									if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
										#JUGADOR MET
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
										self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
										self.data[ self.playerpos[ 0 ] - 2 ][ self.playerpos[ 1 ] ] = const.CAJAM
										return self.data
									else: #LIBRE ACT
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
										self.data[ self.playerpos[ 0 ] - 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
										self.data[ self.playerpos[ 0 ] - 2][ self.playerpos[ 1 ] ] = const.CAJAM
										return self.data
								else:
									return False
			else:
				if (direccion=='S'):
					#Avanzar Abajo
					if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] == const.LIBRE): # Si la siguiente casilla esta libre
						self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
						self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADOR
						return self.data
					else:
						if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] == const.CAJA): # Si en la siguiente casilla hay una caja
							if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.LIBRE): # Si depues de la caja hay vacio
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADOR
								self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJA
								return self.data
							else
								if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.META): # Si despues de la caja hay una meta
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADOR
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJAM
									return self.data
						else:
							if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] == const.CAJAM): #Recordar Jugador sobre meta
								if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.LIBRE): #META CAJA LIBRE
									if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
										#JUGADOR MET
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJA
										return self.data
										
									else: #LIBRE ACT
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJA
										return self.data
								else
									if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] == const.META ):
										if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
											#JUGADOR MET
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJAM
											return self.data
										else: #LIBRE ACT
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 1] = const.JUGADORM
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] - 2] = const.CAJAM
											return self.data
									else:
										return False
				else:
					if (direccion=='D'):
						#Avanzar Derecha
						if ( self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si la siguiente casilla esta libre
							self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
							self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ]] = const.JUGADOR
							return self.data
						else:
							if ( self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] == const.CAJA): # Si en la siguiente casilla hay una caja
								if ( self.data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ]] == const.LIBRE): # Si depues de la caja hay vacio
									self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
									self.data[ self.playerpos[ 0 ] + 1][ self.playerpos[ 1 ] ] = const.JUGADOR
									self.data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] = const.CAJA
									return self.data
								else
									if ( self.data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] == const.META): # Si despues de la caja hay una meta
										self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
										self.data[ self.playerpos[ 0 ] + 1][ self.playerpos[ 1 ] ] = const.JUGADOR
										self.data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] = const.CAJAM
										return self.data
							else:
								if ( self.data[ self.playerpos[ 0 ] + 1][ self.playerpos[ 1 ] ] == const.CAJAM): #Recordar Jugador sobre meta
									if ( self.data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] == const.LIBRE): #META CAJA LIBRE
										if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
											#JUGADOR MET
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
											self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
											self.data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] = const.CAJA
											return self.data
										else: #LIBRE ACT
											self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
											self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
											self.data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] = const.CAJA
											return self.data
									else
										if ( self.data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] == const.META ):
											if ( self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ]] == const.JUGADORM): #ACT META CAJA
												#JUGADOR MET
												self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.META
												self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
												self.data[ self.playerpos[ 0 ] + 2 ][ self.playerpos[ 1 ] ] = const.CAJAM
												return self.data
											else: #LIBRE ACT
												self.data[ self.playerpos[ 0 ] ][ self.playerpos[ 1 ] ] = const.LIBRE
												self.data[ self.playerpos[ 0 ] + 1 ][ self.playerpos[ 1 ] ] = const.JUGADORM
												self.data[ self.playerpos[ 0 ] + 2][ self.playerpos[ 1 ] ] = const.CAJAM
												return self.data
										else:
											return False
					else:
						return self.playerpos
    
    def Print (self):
        print("c")
    
