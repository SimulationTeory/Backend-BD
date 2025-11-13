import math
from scipy.stats import norm 

class Operations:
    """
    Clase encargada de realizar las operaciones estadísticas relacionadas con el método PERT.
    
    Contiene funciones para calcular el tiempo esperado, la varianza individual por actividad 
    y la varianza típica total, además de la probabilidad de cumplir con un tiempo objetivo.
    """

    def calc_te(self, data):
        """
        Calcula el tiempo esperado (TE) de una actividad utilizando la fórmula PERT.

        Args:
            data (dict): Diccionario que contiene los valores 'a' (optimista), 'm' (más probable) y 'b' (pesimista).

        Returns:
            dict: Diccionario original con un nuevo campo 'tiempo pert' que representa el tiempo esperado.
        """
        data["tiempo pert"] = round((data["a"] + 4 * data["m"] + data["b"]) / 6, 3)
        return data

    def calc_varianza(self, data):
        """
        Calcula la varianza de una actividad en el método PERT.

        Args:
            data (dict): Diccionario que contiene los valores 'a' (optimista) y 'b' (pesimista).

        Returns:
            dict: Diccionario original con un nuevo campo 'Varianza' que representa la varianza calculada.
        """
        data["Varianza"] = round(((data["b"] - data["a"]) ** 2) / 36, 3)
        return data
    
    def varianzaTipica(self, edges, graph, max):
        """
        Calcula la varianza típica total y la probabilidad de finalizar el proyecto en un tiempo dado.

        Args:
            edges (list): Lista de arcos (en formato "origen-destino") que representan el camino crítico.
            graph (networkx.DiGraph): Grafo con las aristas que contienen los valores de varianza por actividad.
            max (float): Tiempo máximo estimado del proyecto (por ejemplo, el valor total de semanas).

        Returns:
            dict: Diccionario con:
                - 'varianza': valor de la desviación típica total del proyecto.
                - 'probabilidad': probabilidad acumulada  de terminar en o antes de un tiempo objetivo.
        """
        sumaVarinzas = 0
       
        for edge in edges:
            nodes = edge.split("-")
            nodeI = int(nodes[0])
            nodeF = int(nodes[1])
            sumaVarinzas += graph[nodeI][nodeF]["varianza"] 
            
        varianzaT = round(math.sqrt(sumaVarinzas), 2)
        prob = round(norm.cdf(30, loc=max, scale=varianzaT), 3)

        data = {
            "varianza": varianzaT,
            "probabilidad": float(prob)
        }

        return data
