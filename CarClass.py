class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed_data = 0
    def accelerate(self):
        self.__speed_data += 5
    def brake(self):
        self.__speed_data -= 5
    def get_speed(self):
        return self.__speed_data
    