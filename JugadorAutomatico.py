from Graph import *

class JugadorAutomatico:

    boardData = [[]]
    def __init__(self,boardData):
        self.boardData = boardData

    def armarGrafo(self):
        g = Graph()
        for i in range(0,len(self.boardData[0])):
            for j in range(0,len(self.boardData)):
                node = (i , j)
                g.add_node(node)

        for ver in g.nodes:
            for i in range(0,len(self.boardData[0])):
                for j in range(0,len(self.boardData)):
                    node = (i , j)
                    if j+1 < len(self.boardData):
                        if self.boardData[i][j] == 'X' and self.boardData[i][j+1] == 'X':
                            continue
                        else:
                            aux = (i ,j+1)
                            g.add_edge(node,aux,1)
                    else:
                        continue

        
                        

        
    def print_mat(self):
        for i in range(0,len(self.boardData[0])):
            print(self.boardData[i])

    
