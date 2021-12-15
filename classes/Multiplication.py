import logging
class Multiplication:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def multiplication(self):
        result = 0
        try:
            result = self.num1 * self.num2
            logging.info("Multiplication operation performed")
        except Exception as e:
            logging.info("Multiplication Operation Error", e)
        return result