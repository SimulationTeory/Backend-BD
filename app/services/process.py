import pandas as pd
from app.services.GraphCalcs import GraphCalc
from app.services.Operations import Operations
import networkx as nx
import matplotlib.pyplot as pl

class Process:
    def __init__(self):
        self.graphCalc = GraphCalc()
        self.operations = Operations()

    def processData(self,data):
       
       dt = pd.DataFrame(data.nodes)
       dt.rename(columns={dt.columns[0]:"Nodos"},inplace=True)
       dt["a"] = pd.Series(data.timepo_op)
       dt["m"] = pd.Series(data.tiempo_es)
       dt["b"] = pd.Series(data.tiempo_pe)
       
       dt =  self.operations.calc_te(dt)
       dt = self.operations.calc_varianza(dt)

       graph =  self.creategraph(dt)
    
       early = self.graphCalc.calc_early(graph)
       self.graphCalc.calc_last(graph,early)
       holgura = self.graphCalc.calc_holgura(graph)
      
       return  {"early":f"{early}"}
    
    def creategraph(self,data):
        g = nx.DiGraph()
        nodes = list(data["Nodos"])

        for i in range (0,10) :
            g.add_node(i*10, early=0, last=0, holgura=0)
        
        cont = 0
        for node in nodes :
            weightEdge = data.loc[cont]["tiempo pert"]
            cont = cont +1
            n = node.split("−")
            g.add_edge(int(n[0]),int(n[1]),weight=weightEdge)

        return g

        

    def printGraph(self,graph):
         g = graph
         pos = nx.circular_layout(g)
         weights = nx.get_edge_attributes(g,"weight")
         nx.draw(g,pos,with_labels=True,node_size=800,node_color="lightblue",edge_color="green")
         nx.draw_networkx_edge_labels(g,pos,edge_labels= weights, font_color="red")
         #pl.savefig("grafo.png")
         pl.show()
        
        