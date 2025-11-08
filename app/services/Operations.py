import math
from scipy.stats import norm 

class Operations:

    def __init__(self):
        pass

    def calc_te(self, data):
        data["tiempo pert"] =round( (data["a"] + 4 * data["m"] + data["b"]) / 6,3)
        return data

    def calc_varianza(self, data):
        data["Varianza"] = round(((data["b"] - data["a"]) ** 2) / 36,3)
        return data
    
    def varianzaTipica(self,edges,graph,max):
        sumaVarinzas = 0
       
        for edge in edges:
            nodes = edge.split("-")
            nodeI = int(nodes[0])
            nodeF = int(nodes[1])
            
            sumaVarinzas += graph[nodeI][nodeF]["varianza"] 
            
        varianzaT = round(math.sqrt(sumaVarinzas),2)
        prob = round(norm.cdf(30,loc=max,scale=varianzaT),3)

        data = {
            "varianza":varianzaT,
            "probabilidad":float(prob)
        }

        return data