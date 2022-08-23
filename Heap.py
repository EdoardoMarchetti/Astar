import math
from Node import *


class MinHeap:

    def __init__(self, key):
        self.heap = [Node(-1, -1, -1)] #Nodo fittizzio per far partire gli indici da 1 
        self.heap_size = 0

        if(key == 'g' or key == 'h' or key == 'h+g'):
            self.key = key  #il campo key può valere 'g' = solo costo arco, 'h' = solo eruistica, 'h+g' = costo+euristica
                            #verrà indicata dall'algoritmo 
        else:
            raise Exception("Funzione di costo non valida")
        
    
    def parent(self, i):
        return math.floor(i/2)

    def left(self, i):
        return 2*i
        
    def right(self, i):
        return 2*i + 1

    def is_empty(self):
        return self.heap_size == 0

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)


        min = i

        if l <= self.heap_size and self.heap[l].getKey(self.key) <= self.heap[i].getKey(self.key):
            min = l

        if r <= self.heap_size and self.heap[r].getKey(self.key) <= self.heap[min].getKey(self.key):
            min = r

        if min != i:
            tmp = self.heap[min]
            self.heap[min] = self.heap[i]
            self.heap[i] = tmp

            self.heap[i].handle = i
            self.heap[min].handle = min
            

            self.min_heapify(min)

    
    def minimum(self):
        if self.heap_size == 0:
            raise Exception("Heap vuoto")
        
        return self.heap[1] #in 0 c'è il nodo sentinella


    def insert(self, node):
        
        self.heap.append(node)
        

        self.heap_size = self.heap_size + 1
        i = self.heap_size
        node.handle = i
       
        #Risalgo
        while i > 1 and self.heap[self.parent(i)].getKey(self.key) > self.heap[i].getKey(self.key):
            #Switch
            tmp = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = tmp

            self.heap[i].handle = i
            self.heap[self.parent(i)].handle = self.parent(i)

            i = self.parent(i)
        
        
    def decrease_key(self, node, k):
        if k > node.getKey(self.key):
            raise Exception("Nuova chiave più alta")

        
        node.g = k
        i = node.handle

        
        while i > 1 and self.heap[self.parent(i)].getKey(self.key) > self.heap[i].getKey(self.key):
            tmp = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = tmp

            self.heap[i].handle = i
            self.heap[self.parent(i)].handle = self.parent(i)

            i = self.parent(i)


    def delete(self, node):
        i = node.handle
        self.heap[i] = self.heap[self.heap_size]
        node.handle = -1
        

        self.heap_size = self.heap_size - 1
        self.heap.pop() 
        


        while i > 1 and self.heap[self.parent(i)].getKey(self.key) > self.heap[i].getKey(self.key):
            tmp = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = tmp

            self.heap[i].handle = i
            self.heap[self.parent(i)].handle = self.parent(i)

            i = self.parent(i)
        
        self.min_heapify(i)

    
    def extract_min(self):
        if self.heap_size == 0:
            raise Exception("Coda vuota")

        min = self.heap[1]
        min.handle = -1
        

        self.heap[1] = self.heap[self.heap_size]
        self.heap[1].handle = 1

        self.heap_size = self.heap_size - 1
        self.heap.pop() 

        self.min_heapify(1)

        return min

    
    def print_heap(self):
        print("Heap: ")
        print("heap_size = ", self.heap_size)
        print("heap len = ", len(self.heap) - 1 )
        for i in range(1,self.heap_size+1):
            print("",self.heap[i].getID(),": ",self.heap[i].getKey(self.key),"")


    








    

    
    

