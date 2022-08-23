import numpy as np
from Node import *
from Edge import *

class FileReader:

    @staticmethod
    def prepareLists( nodesFilePath , edgesFilePath ):
        
        nodesFile = open(nodesFilePath, "r")
        edgesFile = open(edgesFilePath, "r")

        nodeList = []
        edgeList = []
        
        #Creazione della lista dei nodi
        for line in nodesFile:
            arr = line.split()
            node = Node(int(arr[0]), float(arr[1]), float(arr[2])) 
            nodeList.append(node)
            

        nodesFile.close()

        #Creazione della lista dei nodi
        for line in edgesFile:
            arr = line.split()
            edge = Edge(int(arr[1]), int(arr[2]), float(arr[3])) 
            edgeList.append(edge)

        edgesFile.close()

        return [nodeList, edgeList]