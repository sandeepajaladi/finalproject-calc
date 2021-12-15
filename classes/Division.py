import logging
class Division:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def division(self):
        result = 0
        try:
            result = self.num1 / self.num2
            logging.info("Division operation performed")
        except Exception as e:
            logging.info("Division Operation Error", e)
        return result