from FileReader import *
from Graph import *
from Problem import *
from Heap import MinHeap
from Algorithms import *
import time



print("Fase 1: ...............Creazione dell liste..................")
edgesFilePath= "Resources/CaliforniaRoadEdge.txt"
nodesFilePath = "Resources/CaliforniaRoadNode.txt"
[nodeList, edgeList] = FileReader.prepareLists(nodesFilePath, edgesFilePath)
print("\nNumero nodi = ", len(nodeList)) #Stampa il numero di nodi che compongono il grafo
print("Numero edge = ", len(edgeList))   #Stampa il numero degli archi che compongono il grafo

# Mappa creata manualmente per fare dei test
# testMapNode =[Node(0, 1, 1), Node(1, 1, 2), Node(2, 2, 3), Node(3, 3, 3), Node(4, 4, 4), Node(5, 6, 3), Node(6, 10, 10)]
#testMapEdge =[Edge(0, 1, 0.1), Edge(1, 2, 0.2), Edge(2, 3, 0.3), Edge(0, 3, 5), Edge(3, 4, 2), Edge(0, 5, 3), Edge(5, 4, 1) ]


print("\nFase 2: ................Creazione del grafo.....................")
graph = Graph(nodeList, edgeList)
graph.print_adj(6)

print("\nFase 3: .............Definizione del problema................")
initialState = 0
goalState = 1000	
problem = Problem(graph, initialState, goalState)



print("\nFase 4: .............Risoluzione problema...............")
ti = time.time()
(result, costo, explored) = greedy_search(problem) #sostituire a_star con ucs(problem) o greedy_search(problem)
tf = time.time()
print("\nFase 5: ....................Stampa dei Risultati.................")
if result == None: #Allora non esite una strada che collega i due punti 
    print("Soluzione non trovata")
else:   #Viene stampata la lista di nodi che compongono la soluzione
    #print("Soluzione  : \n", result)                     #Decommentare se si vuole visualizzare a video la soluzione completa 
    print("Numero nodi della soluzione = ", len(result)) #Stampa del numero dei nodi che compongono la soluzione 
    #print("Lista nodi visitati : \n", explored)         #Decommentare se si vuole visualizzare a video la lista dei nodi esplorati 
    print("Numero nodi visitati = ", len(explored))      #Stampa del numero dei nodi visitati
    print(f"Costo = {costo}")                            #Stampa del costo della soluzione trovata   
print(f"Tempo impiegato = {(tf -ti)} s")                 #Stampa del tempo impiegato per la risoluzione del problema (comprende il tempo impiegao per il calcolo dell'euristica)   

    