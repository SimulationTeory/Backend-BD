class Operations:

    def __init__(self):
        pass

    def calc_te(self, data):
        data["tiempo pert"] = (data["a"] + 4 * data["m"] + data["b"]) / 6
        return data

    def calc_varianza(self, data):
        data["Varianza"] = ((data["b"] - data["a"]) ** 2) / 36
        return data