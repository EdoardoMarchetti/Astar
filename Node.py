import math

class Node:

    def __init__(self, id, x, y, g = math.inf, h= math.inf):
       self.id = id 
       self.x = x
       self.y = y

       self.handle = -1
       
       self.g = g
       self.h = h

       self.color = 'white'

       self.parent = None

    #-------------------#
    #------GETTER-------#
    #-------------------#
    def getID(self):
        return self.id
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getKey(self, keyType):
        if keyType == 'g':
            return self.g
        elif keyType == 'h':
            return self.h
        elif keyType =='h+g':
            return self.h + self.g
    
    def getHeuristic(self):
        return self.h 
    
    def getParent(self):
        return self.getParent
    

    #-------------------#
    #------SETTER-------#
    #-------------------#
    def setCost(self, g):
        self.g = g

    def setHeuristic(self, h):
        self.h = h


    #----------------------#
    #------OTHER FUN-------#
    #----------------------#
    
    #Restituisce la lista cosituita dalle coppie (neighborId, edgeCost)
    def expand(self, problem):
        graph = problem.graph

        adjacent = []

        for (adjId, weight) in graph.adj_list[self.id]:
            adjacent.append((graph.getNode(adjId), weight))
        
        return adjacent


    #Permette di ricostruire la soluzione a partire dal nodo su cui viene invocata
    def solution(self):
        solution = []
        v = self
        while v != None:
            solution.insert(0, v.getID())
            v = v.parent
        
        return solution


    #Stampa dei valori dell'oggetto Node su cui è invocata
    def to_string(self):
        print("Nodo ", self.id, " :\n",
              "x = ", self.x , " y = ", self.y, "\n"
              "handle = ", self.handle, "\n",
              "g = ", self.g,"\n", 
              "h = ", self.h, "\n",
              "tot = ", self.h + self.g,"\n"
              "color = ", self.color, "\n",
              "parent = ", self.parent)

    

        

    

    


     