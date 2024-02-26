import random

class CellPhone:

    def __init__(self,ma,mo,rp):
        self.__manufact = ma
        self.__model = mo
        self.__retail_price = rp

    def set_ma(self,ma):
        self.__manufact = ma

    def set_mo(self,mo):
        self.__model = mo
    
    def set_rp(self,rp):
        self.__retail_price = rp
    def get_ma(self):
        return self.__ma
    def get_mo(self):
        return self.__mo
    def get_rp(self):
        return self.__rp
        