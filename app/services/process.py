import pandas as pd
from app.services.GraphCalcs import GraphCalc
from app.services.Operations import Operations
from app.services.Response import Response
import networkx as nx
import matplotlib.pyplot as pl

class Process:
    def __init__(self):
        self.graphCalc = GraphCalc()
        self.operations = Operations()
        self.respose = Response()

    def processData(self,data):
       
       dt = pd.DataFrame(data.nodes)
       dt.rename(columns={dt.columns[0]:"Nodos"},inplace=True)
       dt["a"] = pd.Series(data.tiempo_op)
       dt["m"] = pd.Series(data.tiempo_es)
       dt["b"] = pd.Series(data.tiempo_pe)
       
       dt =  self.operations.calc_te(dt)
       dt = self.operations.calc_varianza(dt)

       graph =  self.creategraph(dt)

       early = self.graphCalc.calc_early(graph)
       self.graphCalc.calc_last(graph,early)
       holgura = self.graphCalc.calc_holgura(graph)
       crticalPath = self.graphCalc.calCriticalPath(graph)
       
       dataNodes = self.graphCalc.dataGraph(graph)
       self.respose.resposeCaseA(crticalPath,dataNodes)
       
       
       graph2 = graph.copy()
       graph2[20][40]["weight"]= 0

       early = self.graphCalc.calc_early(graph2)
       self.graphCalc.calc_last(graph2,early)
       holgura = self.graphCalc.calc_holgura(graph2)
       result = self.graphCalc.calCriticalPath(graph2)
       crticalPathB = list(result["criticalPath"])
       max = int(result["numero_semanas"])
       
       resultProb = self.operations.varianzaTipica(crticalPathB,graph2,max)
       dataNodes2 = self.graphCalc.dataGraph(graph2)
       self.respose.resposeCaseB(result,resultProb)

       return  self.respose.jsonResponse()
    
    def creategraph(self,data):
        g = nx.DiGraph()
        nodes = list(data["Nodos"])

        for i in range (0,10) :
            g.add_node(i*10, early=0, last=0, holgura=0)
        
        cont = 0
        for node in nodes :
            weightEdge = data.loc[cont]["tiempo pert"]
            varianza = data.loc[cont]["Varianza"]
            cont = cont +1
            n = node.split("−")
            g.add_edge(int(n[0]),int(n[1]),weight=weightEdge,varianza=varianza)
            
      
        return g

    