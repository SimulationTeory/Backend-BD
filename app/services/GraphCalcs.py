import networkx as nx 
class GraphCalc:

    def calc_early(self, graph):
       
        for node in graph.nodes:
            graph.nodes[node]["early"] = 0

        listNodes = nx.topological_sort(graph)
        
        for node in listNodes:
            predecesores = list(graph.predecessors(node))
            if not predecesores:
                graph.nodes[node]["early"] = 0.0
            else:
                
                early = 0
                for origen in predecesores:
                    
                    peso = graph[origen][node]["weight"]
                    value_early = round(graph.nodes[origen]["early"] + peso,3)
                    if value_early > early:
                        early = value_early
                graph.nodes[node]["early"] = early

        return graph.nodes[90]["early"]
    
    
    def calc_last(self,graph,max):

        for node in graph.nodes :
            graph.nodes[node]["last"] = 0
        
        listNodes = reversed( list(nx.topological_sort(graph)))

        for node in listNodes :

            predecesores = list(graph.successors(node))
            if not predecesores :
                graph.nodes[node]["last"] = max
            else:
                lastValue = max+1
                for sucesor in predecesores :
                   
                    peso = graph[node][sucesor]["weight"]
                    
                    if node  != 0:
                     value = round( graph.nodes[sucesor]["last"]  - peso,3)
                     if value < lastValue:
                        lastValue = value
                     graph.nodes[node]["last"] = float(lastValue)
                    else:
                        graph.nodes[0]["last"] = float(0)

        return None
    
    def calc_holgura(self,graph):

        for node in graph :
            graph.nodes[node]["holgura"] = round(graph.nodes[node]["last"] - graph.nodes[node]["early"],3) 
           

    def calCriticalPath(self,graph):

        nodes = nx.topological_sort(graph)
        criticalPath = {}
        
        for node in nodes:

            sucesores = graph.successors(node)
            

            for nodef in sucesores:
                

                if (graph.nodes[node]["holgura"] == 0) and ( graph.nodes[nodef]["holgura"] == 0):
                    
                    criticalPath[f"{node}-{nodef}"] = {"nodeI":node,"nodeF":nodef,"weight":graph[node][nodef]["weight"]}
        
        g = nx.DiGraph()

        for edge,values in criticalPath.items():
            g.add_edge(values["nodeI"],values["nodeF"],weight=values["weight"])
        
        numero_semanas = round(nx.dag_longest_path_length(g,weight="weight"),2)
        ruta = nx.dag_longest_path(graph,weight="weight")
        path = []
        for i in range(0,len(ruta)-1):
            path.append(f"{ruta[i]}-{ruta[i+1]}")
        
        data = {
            "numero_semanas" : float(numero_semanas),
            "criticalPath": path
        }
        return data
    



    

        
            

        

            


            


         

