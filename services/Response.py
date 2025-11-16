class Response:
    """
    Clase que construye y organiza las respuestas de los diferentes casos
    de simulación del proyecto . 
    """
  

    def __init__(self):
        """Inicializa el objeto Response con un diccionario vacío para almacenar los resultados."""
        self.response = {}
        
      
        
    
    def resposeCaseA(self, data, nodeData,graph):
        """
        Genera la respuesta para el Caso A de la simulación.

        Args:
            data (dict): Contiene los datos generales del resultado, como número de semanas y camino crítico.
            nodeData (dict): Contiene la información detallada de los nodos, incluyendo tiempos y holguras.
        """
        # Información general del caso A
        self.response["SemanasC1"] = data["numero_semanas"]
        self.response["pathA"] = data["criticalPath"]
        self.nodesData(data, nodeData, "A")
        self.tiemposPert(graph,"A")

    def resposeCaseB(self, data, resultProb, nodeData,graph):
        """
        Genera la respuesta para el Caso B de la simulación.

        Args:
            data (dict): Contiene los datos generales del resultado, como número de semanas y camino crítico.
            resultProb (dict): Contiene los resultados estadísticos como varianza y probabilidad.
            nodeData (dict): Contiene la información detallada de los nodos, incluyendo tiempos y holguras.
        """
        # Información del caso B (probabilidad, varianza, etc.)
        self.response["SemanasC2"] = data["numero_semanas"]
        self.response["pathB"] = data["criticalPath"]
        self.response["varianza"] = resultProb["varianza"]
        self.response["probabilidad"] = resultProb["probabilidad"]
        self.nodesData(data, nodeData, "B")
        self.tiemposPert(graph,"B")

    def nodesData(self, data, nodeData, case):
        """
        Agrega información detallada de los nodos para el caso especificado.

        Args:
            data (dict): Contiene información del camino crítico.
            nodeData (dict): Diccionario con datos de cada nodo (early, last, holgura).
            case (str): Identificador del caso ('A' o 'B').
        """
    
        # Identificar los nodos críticos a partir de los arcos críticos
        critical_edges = set(data["criticalPath"])
        critical_nodes = set()
        for edge in critical_edges:
            start, end = map(int, edge.split("-"))
            critical_nodes.add(start)
            critical_nodes.add(end)

        # Agregar información detallada por nodo
        self.response[f"nodes{case}"] = []
        for node_id, info in nodeData.items():
            nid = int(node_id)
            self.response[f"nodes{case}"].append({
                "id": nid,
                "early": info.get("early", 0),
                "latest": info.get("last", 0),
                "holgura": info.get("holgura", 0),
                "critical": nid in critical_nodes
            })
    
    def tiemposPert(self, graph, case):
     """
     Extrae los tiempos PERT (pesos) de las aristas del grafo y los almacena 
     en el diccionario de respuesta bajo la clave correspondiente al caso.

     Args:
        graph (networkx.DiGraph): Grafo que contiene los pesos en sus aristas.
        case (str): Identificador del caso (por ejemplo, 'A' o 'B') para
                    almacenar los datos bajo la clave "timposPert_case".
     """
     
     tiemposPert = {}

     for nodeA, nodeB in graph.edges():
        te = graph.edges[nodeA, nodeB].get("weight")
        tiemposPert[f"{nodeA}-{nodeB}"] = te

     self.response[f"tiemposPert_{case}"] = tiemposPert
     print(self.response[f"tiemposPert_{case}"] )


        
    

    def jsonResponse(self):
        """
        Retorna toda la respuesta combinada lista para ser enviada como JSON.

        Returns:
            dict: Diccionario con todos los resultados del caso o casos procesados.
        """
        # Retornar toda la respuesta combinada
        return self.response

 