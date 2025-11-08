

class Response:

    def __init__(self):
        self.response = {}
    
    def resposeCaseA(self,data):
        self.response["SemanasC1"] = data["numero_semanas"]
        self.response["pathA"] = list(data["criticalPath"])
   
    def resposeCaseB(self,data,resultProb):
        self.response["SemanasC2"]= data["numero_semanas"]
        self.response["pathB"] = list(data["criticalPath"])
        self.response["varianza"] = resultProb["varianza"]
        self.response["probabilidad"] = resultProb["probabilidad"]

    def jsonResponse(self):
        return self.response
    

