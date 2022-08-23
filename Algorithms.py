from Heap import MinHeap
from Problem import Problem
import math


def ucs(problem):
    return best_first(problem, f = 'g')

def greedy_search(problem):
    problem.computeHeuristic()
    return best_first(problem, f = 'h')

def a_star(problem):
    problem.computeHeuristic()
    return best_first(problem, f = 'h+g')
           


def best_first(problem, f = 'g'): 

    if problem.goalState == problem.initialState:                   #Verifica se initialState è anche il goalState
        return (problem.initialState.solution(), 0, [])

    frontier = MinHeap(f)                                           #Inizializzazione della coda di priorità 
    frontier.insert(problem.initialState)                   
    explored = set()                                                #Creazione della lista explored (non strettamente necessaria al fine dell'esecuzione della procedura)

    while not frontier.is_empty():
        node = frontier.extract_min()                               #Estrazione del nodo a chiave minima

        explored.add(node.getID())                          
        node.color = 'black'                                        #Colorazione del nodo per segnarlo come "esplorato"

        if problem.goalState == node:                               #Verifica se il nodo estratto è il nodo che rappresenta goalState
            return (node.solution(), node.g, explored)
        
        
       
        for [neighbor, edgeCost] in node.expand(problem):           #Fase di expand
            
            if neighbor.color == 'white':                           #Nodo mai incontrato
                #Aggiungo il nodo a frontier
                neighbor.color = 'gray'                             #Colorazione del nodo per indicarlo come in frontier
                neighbor.parent = node                              #Aggiornamento del genitore del nodo    
                neighbor.g = neighbor.parent.g + edgeCost           #Impostazione del valore di g(n)

                frontier.insert(neighbor)                           #Inserimento del nodo in frontier
            
            elif neighbor.color == 'gray':                          #Nodo già presente in frontier 
                #Nodo in frontier
                if neighbor.g > node.g + edgeCost:                  #Fase di relax (necessaria solo se f != 'h' in qunato l'euristica non va ad incidere sul perocrso fatti fino a quel momento  )
                    neighbor.parent = node                          #Aggiornamento del genitore del nodo 
                    neighbor.g = node.g + edgeCost                  #Impostazione del valore di g(n)
                    frontier.decrease_key(neighbor, neighbor.g)     #Riposizionamento del frontier in base al nuovo vaolre di g(n)
                
    return (None, math.inf, explored)