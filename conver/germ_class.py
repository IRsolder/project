class Germ:
    def __init__(self,data_from,data_to,value):
        self.data_from = data_from
        self.data_to = data_to
        self.value = value

    def __Germ_gr(self):
        res = 0
        if self.data_to =="gr":
            res = self.value
        elif self.data_to == "kg":
            res = self.value / 1000
        elif self.data_to == "ton":
            res = self.value / 1000 / 1000
        return res

    def __Germ_kg(self):
        res = 0
        if self.data_to =="gr":
            res = self.value * 1000
        elif self.data_to == "kg":
            res = self.value
        elif self.data_to == "ton":
            res = self.value / 1000
        return res

    def __Germ_ton(self):
        res = 0
        if self.data_to =="gr":
            res = self.value * 1000 * 1000
        elif self.data_to == "kg":
            res = self.value * 1000
        elif self.data_to == "ton":
            res = self.value
        return res
    def Germ(self):
        if self.data_from == "gr":
            return self.__Germ_gr()
        elif self.data_from == "kg":
            return self.__Germ_kg()
        elif self.data_from == "ton":
            return self.__Germ_ton()