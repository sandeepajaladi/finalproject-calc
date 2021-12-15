import logging
class Addition:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    def addition(self):
        result = 0
        try:
            result = self.num1 + self.num2
            logging.info("Addion operation performed")
        except Exception as e:
            logging.info("Addition OPeration Error", e)
        return result
    