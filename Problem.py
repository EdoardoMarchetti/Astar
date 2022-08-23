import math

class Problem:

    def __init__(self, graph, initialState, goalState):
        self.graph = graph
        self.initialState = graph.getNode(initialState)
        self.goalState = graph.getNode(goalState)

        self.initialState.g = 0

        #Stampa del nodo iniziale e finale per verificare che il problema è stato inializzato 
        print("\nStart:")
        self.initialState.to_string()
        
        print("\nGoal:")
        self.goalState.to_string()
        


    #-------------------#
    #------GETTER-------#
    #-------------------#
    def getInitialState(self):
        return self.initialState

    def getGoalState(self):
        return self.goalState

    
    #-------------------#
    #-----OTHER FUN-----#
    #-------------------#

    #Calcolo delle euristche per ogni nodo
    def computeHeuristic(self):
        
        self.goalState.setHeuristic(0)

        for node in self.graph.getNodeMatrix():
            if  node != self.goalState:

                h = math.sqrt( (node.getX() - self.goalState.getX())**2 + (node.getY() - self.goalState.getY())**2 )
                node.setHeuristic(h)

    
    def print_heuristic(self, numLines):
        print("\n\n......Esempi di eristiche......")
        print("La tupla indica (nodo, h)")
        i = 0
        while i < numLines:
            print(self.graph.getNode(i).getID(),":", self.graph.getNode(i).getHeuristic())
            i = i+1
                

        


    