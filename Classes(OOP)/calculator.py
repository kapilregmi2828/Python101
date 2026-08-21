# __validate() method is an internal helper method. It checks and validates a value. 

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num): # __validate() method used to validate the num
        if not isinstance(num,(int, float)): # isinstance checks the value's data type. 
            return False
        return True
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid Number.")

calc = Calculator()
calc.add(10)
calc.add(3)
print(calc.result)