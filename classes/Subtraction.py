import logging
class Subtraction:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def subtraction(self):
        result = 0
        try:
            result = self.num1 - self.num2
            logging.info("Subtraction operation performed")
        except Exception as e:
            logging.info("Subtraction Operation Error", e)
        return result