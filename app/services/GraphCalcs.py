import networkx as nx 
class GraphCalc:


    
    def calc_early(self, graph):
       
        for node in graph.nodes:
            graph.nodes[node]["early"] = 0

        listNodes = nx.topological_sort(graph)
        
        for node in listNodes:
            predecesores = list(graph.predecessors(node))
            if not predecesores:
                graph.nodes[node]["early"] = 0
            else:
                
                early = 0
                for origen in predecesores:
                    peso = graph[origen][node]["weight"]
                    value_early = graph.nodes[origen]["early"] + peso
                    if value_early > early:
                        early = value_early
                graph.nodes[node]["early"] = early
 
        
        early_values = {n: graph.nodes[n]["early"] for n in graph.nodes}
        print(early_values)
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
                lastValue = max
                for sucesor in predecesores :

                    peso = graph[node][sucesor]["weight"] 
                    value =  graph.nodes[sucesor]["last"]  - peso
                    if value < lastValue:
                        lastValue = value
                graph.nodes[node]["last"] = int(lastValue)

        last_values = {n: graph.nodes[n]["last"] for n in graph.nodes}
        print("VALORES LAST:", last_values)

        return None
    
    def calc_holgura(self,graph):

        for node in graph :

            graph.nodes[node]["holgura"] = graph.nodes[node]["last"]- graph.nodes[node]["early"]
            
            


            


         

