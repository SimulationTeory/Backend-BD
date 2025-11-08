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
                print(f"{node} = {graph.nodes[node]["early"] }","early")

        return graph.nodes[90]["early"]
    
    
    def calc_last(self,graph,max):
        print(max,"max")

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

                print(graph.nodes[node]["last"],f"{node} last")
                

        
        

        return None
    
    def calc_holgura(self,graph):

        for node in graph :

            graph.nodes[node]["holgura"] = round(graph.nodes[node]["last"] - graph.nodes[node]["early"],3) 
            print( f"{node} = {graph.nodes[node]["holgura"]} = {graph.nodes[node]["last"]} - {graph.nodes[node]["early"]} ","holgura")
           

    def calCriticalPath(self,graph):

        nodes = nx.topological_sort(graph)
        criticalPath = {}
        
        for node in nodes:

            sucesores = graph.successors(node)
            

            for nodef in sucesores:
                

                if (graph.nodes[node]["holgura"] == 0) and ( graph.nodes[nodef]["holgura"] == 0):
                    
                    criticalPath[f"{node}-{nodef}"] = {"nodeI":node,"nodeF":nodef,"weight":graph[node][nodef]["weight"]}
        
        print(criticalPath,"22")
        g = nx.DiGraph()

        for edge,values in criticalPath.items():
            g.add_edge(values["nodeI"],values["nodeF"],weight=values["weight"])
        
        max = round(nx.dag_longest_path_length(g,weight="weight"),2)
        print(max)


    

        
            

        

            


            


         

