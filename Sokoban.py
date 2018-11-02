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
    
