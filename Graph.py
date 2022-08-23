import numpy as np
from Edge import *
#from Node import *

class Graph:

    def __init__(self, nodesMatrix, edgesMatrix):
        self.nodes = nodesMatrix                                                                            #creo una lista con solo gli id dei nodi
        self.adj_list = {}

        #Iniziazlizzo le liste per ogni nodo 
        for node in self.nodes:
            self.adj_list[node.getID()] = []
        
        for edge in edgesMatrix:
            self.add_edge(edge)

    

    #-------------------#
    #------GETTER-------#
    #-------------------#
    def getNode(self, id):
        return self.nodes[id]
    
    def getNodeMatrix(self):
        return self.nodes

    #-------------------#
    #-----OTHER FUN-----#
    #-------------------#
    def add_edge(self, edge):
        #Ricavo le caratteristiche dell'arco
        u = edge.getStartNode()
        v = edge.getEndNode()
        w = edge.getWeight()

        self.adj_list[u].append((v,w)) #Affianco all'ID del vertice adiacente salvo il peso dell'arco
        self.adj_list[v].append((u,w))


    
    def print_adj(self, numLines):
        print(f"Prime {numLines} righe del grafo")
        print("La tupla definisce (adiacente, peso_arco)")
        i = 0
        while i < numLines:
            print(self.nodes[i].getID(),":", self.adj_list[self.nodes[i].getID()])
            i = i+1
    
        
    
    

        






    
                    