class Response:

    def __init__(self):
        self.response = {}
    
    def resposeCaseA(self, data, nodeData):
        # Información general del caso A
        self.response["SemanasC1"] = data["numero_semanas"]
        self.response["pathA"] = data["criticalPath"]

        # Identificar los nodos críticos a partir de los arcos críticos
        critical_edges = set(data["criticalPath"])
        critical_nodes = set()
        for edge in critical_edges:
            start, end = map(int, edge.split("-"))
            critical_nodes.add(start)
            critical_nodes.add(end)

        # Agregar información detallada por nodo
        self.response["nodes"] = []
        for node_id, info in nodeData.items():
            nid = int(node_id)
            self.response["nodes"].append({
                "id": nid,
                "early": info.get("early", 0),
                "latest": info.get("last", 0),
                "holgura": info.get("holgura", 0),
                "critical": nid in critical_nodes
            })

    def resposeCaseB(self, data, resultProb):
        # Información del caso B (probabilidad, varianza, etc.)
        self.response["SemanasC2"] = data["numero_semanas"]
        self.response["pathB"] = data["criticalPath"]
        self.response["varianza"] = resultProb["varianza"]
        self.response["probabilidad"] = resultProb["probabilidad"]

    def jsonResponse(self):
        # Retornar toda la respuesta combinada
        return self.response
