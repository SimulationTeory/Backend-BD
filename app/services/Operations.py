class Operations:

    def __init__(self):
        pass

    def calc_te(self, data):
        data["tiempo pert"] =round( (data["a"] + 4 * data["m"] + data["b"]) / 6,3)
        print(data["tiempo pert"])
        return data

    def calc_varianza(self, data):
        data["Varianza"] = round(((data["b"] - data["a"]) ** 2) / 36,3)
        print(data["Varianza"])
        return data