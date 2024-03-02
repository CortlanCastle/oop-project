class CellPhone:


    def __init__(self, manufacturer,model_number, retail_price):
        self.__manufact = manufacturer
        self.__model = model_number
        self.retail_price = retail_price
    def set_manufact (self, manufacturer):
        self.__manufact = manufacturer
    def set_model(self, model_number):      
        self.__model = model_number
    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price
    def get_manufact (self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price
        