from datetime import date

class Student:
    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification.lower()
        self.__age = 0
        self.__register = ''

    def calculate_age(self):
        today = date.today()
        dob_date = self.__dob.split('/')
        dob_year = int(dob_date[2])
        age = today.year - dob_year
        return age
    
    def determine_registration_date(self):
        if self.__classification == "senior":
            return "April 1 - April 3"
        elif self.__classification == "junior":
            return "April 4 - April 6"
        elif self.__classification == "sophomore":
            return "April 7 - April 9:"
        elif self.__classification == "freshman":
            return "April 10 - April 12"
        else:
            return "classification not found"
        
    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_classification(self):
        return self.__classification
    


    

