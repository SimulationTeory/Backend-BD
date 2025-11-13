import networkx as nx 

class GraphCalc:
    """
    Clase encargada de realizar los cálculos principales sobre un grafo dirigido 
    incluyendo el cálculo de tiempos tempranos, tiempos tardíos, holguras y camino crítico.
    """

    def calc_early(self, graph):
        """
        Calcula el tiempo más temprano  para cada nodo del grafo.

        Recorre el grafo en orden topológico, asignando a cada nodo el valor más alto 
        entre la suma del tiempo temprano y el peso de sus aristas entrantes. 
        Los nodos sin predecesores comienzan con tiempo 0.

        Args:
            graph (networkx.DiGraph): Grafo dirigido con pesos en las aristas.

        Returns:
            float: Valor del tiempo más temprano del nodo final.
        """
        # Inicializar todos los tiempos tempranos en 0
        for node in graph.nodes:
            graph.nodes[node]["early"] = 0

        dataEarly = []
        listNodes = nx.topological_sort(graph)

        for node in listNodes:
            predecesores = list(graph.predecessors(node))
            if not predecesores:
                graph.nodes[node]["early"] = 0.0
                dataEarly.append(0.0)
            else:
                early = 0
                for origen in predecesores:
                    peso = graph[origen][node]["weight"]
                    value_early = round(graph.nodes[origen]["early"] + peso, 3)
                    if value_early > early:
                        early = value_early
                graph.nodes[node]["early"] = early
                dataEarly.append(early)

        return graph.nodes[90]["early"]

    def calc_last(self, graph, max):
        """
        Calcula el tiempo más tardío  para cada nodo del grafo.

        Recorre el grafo en orden topológico inverso, asignando el menor valor posible 
        de los tiempos tardíos considerando los sucesores y los pesos de las aristas.

        Args:
            graph (networkx.DiGraph): Grafo dirigido con pesos en las aristas.
            max (float): Valor del tiempo máximo 
        """
        # Inicializar todos los tiempos tardíos en 0
        for node in graph.nodes:
            graph.nodes[node]["last"] = 0

        listNodes = reversed(list(nx.topological_sort(graph)))

        for node in listNodes:
            predecesores = list(graph.successors(node))
            if not predecesores:
                graph.nodes[node]["last"] = max
            else:
                lastValue = max + 1
                for sucesor in predecesores:
                    peso = graph[node][sucesor]["weight"]
                    if node != 0:
                        value = round(graph.nodes[sucesor]["last"] - peso, 3)
                        if value < lastValue:
                            lastValue = value
                        graph.nodes[node]["last"] = float(lastValue)
                    else:
                        graph.nodes[0]["last"] = float(0)

    def calc_holgura(self, graph):
        """
        Calcula la holgura total de cada nodo del grafo.

        La holgura se obtiene restando el tiempo temprano del tiempo tardío de cada nodo.

        Args:
            graph (networkx.DiGraph): Grafo dirigido con tiempos tempranos y tardíos.

       
        """
        for node in graph:
            graph.nodes[node]["holgura"] = round(
                graph.nodes[node]["last"] - graph.nodes[node]["early"], 3
            )

    def calCriticalPath(self, graph):
        """
        Calcula el camino crítico del proyecto a partir de los valores de holgura.

        Identifica las aristas y nodos con holgura cero, y determina el camino 
        más largo en el grafo.

        Args:
            graph (networkx.DiGraph): Grafo dirigido con tiempos calculados.

        Returns:
            dict: Contiene el número total de semanas y la lista de arcos del camino crítico.
        """
        nodes = nx.topological_sort(graph)
        criticalPath = {}

        for node in nodes:
            sucesores = graph.successors(node)
            for nodef in sucesores:
                if (graph.nodes[node]["holgura"] == 0) and (graph.nodes[nodef]["holgura"] == 0):
                    criticalPath[f"{node}-{nodef}"] = {
                        "nodeI": node,
                        "nodeF": nodef,
                        "weight": graph[node][nodef]["weight"]
                    }

        # Crear un subgrafo con los arcos críticos
        g = nx.DiGraph()
        for edge, values in criticalPath.items():
            g.add_edge(values["nodeI"], values["nodeF"], weight=values["weight"])

        numero_semanas = round(nx.dag_longest_path_length(g, weight="weight"), 2)
        ruta = nx.dag_longest_path(graph, weight="weight")

        # Crear lista con las conexiones del camino crítico
        path = []
        for i in range(0, len(ruta) - 1):
            path.append(f"{ruta[i]}-{ruta[i + 1]}")

        data = {
            "numero_semanas": float(numero_semanas),
            "criticalPath": path
        }
        return data

    def dataGraph(self, graph):
        """
        Extrae los datos relevantes de cada nodo del grafo (early, last, holgura).

        Args:
            graph (networkx.DiGraph): Grafo con los cálculos realizados.

        Returns:
            dict: Diccionario con la información de cada nodo.
        """
        data = {}
        nodes = graph.nodes()

        for node in nodes:
            data[f"{node}"] = {
                "early": float(graph.nodes[node]["early"]),
                "last": float(graph.nodes[node]["last"]),
                "holgura": float(graph.nodes[node]["holgura"])
            }
    
     
        return data
