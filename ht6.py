class Calc(object):
    """last_result it is variable where will be saved result of calculation, by default is None"""
    last_result = None

    """these are methods that take 2 arguments a and b and execute corresponding operations with these arguments, 
    then set the last_result variable to the result of the execution of the operation
    
    """
    def add(self, a, b):
        self.last_result = a + b

    def subtract(self, a, b):
        self.last_result = a - b

    def multiply(self, a, b):
        self.last_result = a * b

    def divide(self, a, b):
        try:
            self.last_result = a / b
        except ZeroDivisionError:
            self.last_result = 0
            print("Zerro division error!")


clc = Calc()
print(clc.last_result)
clc.add(3, 2)
print(clc.last_result)
