class Edge:

    def __init__(self, start, end, weight):
       self.startNode = start 
       self.endNode = end
       self.weight = weight

    def getStartNode(self):
        return self.startNode
    
    def getEndNode(self):
        return self.endNode

    def getWeight(self):
        return self.weight